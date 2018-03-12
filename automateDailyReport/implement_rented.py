import pyexcel as pe
import csv
import json
from datetime import date, timedelta

def transform_data_implement(input_file, yesterday):
    input_csv = csv.DictReader(open(input_file))

    count_hours = 0
    count_orders = 0
    implement_reports = {}

    for row in input_csv:
        # if row["Start Date"] == yesterday.strftime('%d/%m/%Y'):
        implement_reports[row["State Name"]] = implement_reports.get(row["State Name"]) or {}
        
        implement_reports[row["State Name"]]["Total"] = implement_reports.get(row["State Name"]).get("Total") or {}
        implement_reports[row["State Name"]]["Total"]["Hours"] = implement_reports.get(row["State Name"]).get("Total").get("Hours") or 0
        implement_reports[row["State Name"]]["Total"]["Hours"] = implement_reports.get(row["State Name"]).get("Total").get("Hours") + round(float(row["No of Hour"]), 2)
        implement_reports[row["State Name"]]["Total"]["Orders"] = implement_reports.get(row["State Name"]).get("Total").get("Orders") or 0
        implement_reports[row["State Name"]]["Total"]["Orders"] = implement_reports.get(row["State Name"]).get("Total").get("Orders") + 1
        
        implement_reports[row["State Name"]]["C2Cs on New Platform"] = implement_reports.get(row["State Name"]).get("C2Cs on New Platform") or {}
        implement_reports[row["State Name"]]["C2Cs on New Platform"]["Hours"] = implement_reports.get(row["State Name"]).get("C2Cs on New Platform").get("Hours") or 0
        implement_reports[row["State Name"]]["C2Cs on New Platform"]["Orders"] = implement_reports.get(row["State Name"]).get("C2Cs on New Platform").get("Orders") or 0
        
        implement_reports[row["State Name"]][row["Hub Name"]] = implement_reports.get(row["State Name"]).get(row["Hub Name"]) or {}
        implement_reports[row["State Name"]][row["Hub Name"]]["Completed Hrs"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Completed Hrs") or 0
        implement_reports[row["State Name"]][row["Hub Name"]]["Count"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Count") or 0

        implement_reports[row["State Name"]][row["Hub Name"]]["Completed Hrs"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Completed Hrs") + round(float(row["No of Hour"]), 2)
        implement_reports[row["State Name"]][row["Hub Name"]]["Count"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Count") + 1
        count_hours += round(float(row["No of Hour"]), 2)
        count_orders += 1
    
    implement_reports["Total"] = implement_reports.get("Total") or {}
    implement_reports["Total"]["Hours"] = count_hours
    implement_reports["Total"]["Orders"] = count_orders
    print("implement total hours    ="+format(count_hours))
    print("implement total orders   ="+format(count_orders))

    with open("implement_rented.json" , 'w') as f:
        json.dump(implement_reports, f)
    
    return implement_reports


def transform_data_implement_new_pf(implements_old_pf, fname, yesterday):
    implements = {}
    sheet = pe.get_sheet(file_name=fname)
    first_row = sheet.row_at(0)
    state_index = first_row.index("Suplier State")
    hub_index = first_row.index("Hub")
    order_date_index = first_row.index("Order Date")
    status_index = first_row.index("Status")
    driver_type_index = first_row.index("Driver Type")
    time_index = first_row.index("Minutes")
    sku_index = first_row.index("sku_repr")
    sheet.name_columns_by_row(0)

    implements_orders = 0
    implements_hours = 0

    today = date.today()
    yesterday = date.today() - timedelta(1)
    print(yesterday)
    yesterday_date = int(yesterday.strftime("%d"))
    dates = []
    for i in range(1, yesterday_date+1):
        print(i)
        dates.append((date.today() - timedelta(i)).strftime("%d/%m/%Y"))

    for state in implements_old_pf:
        implements[state] = implements.get(state) or {}
        if state != "Total":
            for hub in implements_old_pf[state]:
                if hub != "Total":
                    implements[state][hub] = implements.get(state).get(hub) or {}
                    implements[state][hub]["Completed Hrs"] = implements.get(state).get(hub).get("Completed Hrs") or 0
                    implements[state][hub]["Count"] = implements.get(state).get(hub).get("Count")
                    implements[state][hub]["Completed Hrs"] = implements_old_pf.get(state).get(hub).get("Completed Hrs")
                    implements[state][hub]["Count"] = implements_old_pf.get(state).get(hub).get("Count")
                else:
                    implements[state]["Total"] = implements.get(state).get("Total") or {}
                    implements[state]["Total"]["Hours"] = implements.get(state).get("Total").get("Hours") or 0
                    implements[state]["Total"]["Orders"] = implements.get(state).get("Total").get("Orders") or 0
                    implements[state]["Total"]["Hours"] = implements_old_pf.get(state).get("Total").get("Hours")
                    implements[state]["Total"]["Orders"] = implements_old_pf.get(state).get("Total").get("Orders")
        else:
            implements["Total"] = implements.get("Total") or {}
            implements["Total"]["Hours"] = implements.get("Total").get("Hours") or 0
            implements["Total"]["Orders"] = implements.get("Total").get("Orders") or 0
            implements["Total"]["Hours"] = implements_old_pf.get("Total").get("Hours")
            implements["Total"]["Orders"] = implements_old_pf.get("Total").get("Orders")

    for row in sheet:
        if ((yesterday.strftime("%m/%Y") in row[order_date_index] and row[order_date_index] in dates) and (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index] == "Partially Paid" or row[status_index] == "Work Completed"
         or row[status_index] == "Closed" or row[status_index] == "Feedback" or row[status_index] == "Work Started") 
         and (row[time_index] != "" and (int(row[time_index]) > 9)) 
         and (row[sku_index] != "" and (row[sku_index][-1] == "2" or row[sku_index][-1] == "1"))):

            if row[hub_index] == "Dahegam" and row[state_index] == "india":
                state = row[first_row.index("Suplier District")].title()
            else:
                state = row[state_index].title() 
            
            implements_orders += 1
            implements_hours += round(round(float(row[time_index])/60, 2), 2)
            
            implements[state] = implements.get(state) or {}
            implements[state]["Total"] = implements.get(state).get("Total") or {}
            implements[state]["Total"]["Orders"] = implements.get(state).get("Total").get("Orders") or 0
            implements[state]["Total"]["Hours"] = implements.get(state).get("Total").get("Hours") or 0
            implements[state]["Total"]["Orders"] = implements.get(state).get("Total").get("Orders") + 1
            implements[state]["Total"]["Hours"] = implements.get(state).get("Total").get("Hours") + round(float(row[time_index])/60, 2)

            implements[state]["C2Cs on New Platform"] = implements.get(state).get("C2Cs on New Platform") or {}
            implements[state]["C2Cs on New Platform"]["Hours"] = implements.get(state).get("C2Cs on New Platform").get("Hours") or 0
            implements[state]["C2Cs on New Platform"]["Orders"] = implements.get(state).get("C2Cs on New Platform").get("Orders") or 0

            if row[hub_index] == "":
                implements[state]["C2Cs on New Platform"]["Hours"] = implements.get(state).get("C2Cs on New Platform").get("Hours") + round(float(row[time_index])/60, 2)
                implements[state]["C2Cs on New Platform"]["Orders"] = implements.get(state).get("C2Cs on New Platform").get("Orders") + 1    
            else:
                implements[state][row[hub_index]] = implements.get(state).get(row[hub_index]) or {}
                implements[state][row[hub_index]]["Completed Hrs"] = implements.get(state).get(row[hub_index]).get("Completed Hrs") or 0
                implements[state][row[hub_index]]["Count"] = implements.get(state).get(row[hub_index]).get("Count") or 0

                if row[driver_type_index] == "HUB":
                    implements[state][row[hub_index]]["Completed Hrs"] = implements.get(state).get(row[hub_index]).get("Completed Hrs") + round(float(row[time_index])/60, 2)
                    implements[state][row[hub_index]]["Count"] = implements.get(state).get(row[hub_index]).get("Count") + 1

    implements["Total"] = implements.get("Total") or {}
    implements["Total"]["Hours"] = implements.get("Total").get("Hours") or 0
    implements["Total"]["Orders"] = implements.get("Total").get("Orders") or 0
    implements["Total"]["Hours"] = implements.get("Total").get("Hours") + implements_hours
    implements["Total"]["Orders"] = implements.get("Total").get("Orders") + implements_orders
    
    print("new pf implements =   " + format(implements_orders))
    print("new pf implement hours =   " + format(implements_hours))

    return implements