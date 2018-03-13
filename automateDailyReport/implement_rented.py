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
        state = row["State Name"]
        hub = row["Hub Name"]
        district = row["District Name"]
        # if row["Start Date"] == yesterday.strftime('%d/%m/%Y'):
        implement_reports[state] = implement_reports.get(state) or {}
        
        implement_reports[state]["Total"] = implement_reports.get(state).get("Total") or {}
        implement_reports[state]["Total"]["Hours"] = implement_reports.get(state).get("Total").get("Hours") or 0
        implement_reports[state]["Total"]["Hours"] = implement_reports.get(state).get("Total").get("Hours") + round(float(row["No of Hour"]), 2)
        implement_reports[state]["Total"]["Orders"] = implement_reports.get(state).get("Total").get("Orders") or 0
        implement_reports[state]["Total"]["Orders"] = implement_reports.get(state).get("Total").get("Orders") + 1
        
        implement_reports[state]["C2Cs on New Platform"] = implement_reports.get(state).get("C2Cs on New Platform") or {}
        implement_reports[state]["C2Cs on New Platform"]["Hours"] = implement_reports.get(state).get("C2Cs on New Platform").get("Hours") or 0
        implement_reports[state]["C2Cs on New Platform"]["Orders"] = implement_reports.get(state).get("C2Cs on New Platform").get("Orders") or 0
        

        implement_reports[state][district] = implement_reports.get(state).get(district) or {}
        
        implement_reports[state][district]["Total"] = implement_reports.get(state).get(district).get("Total") or {}
        implement_reports[state][district]["Total"]["Hours"] = implement_reports.get(state).get(district).get("Total").get("Hours") or 0
        implement_reports[state][district]["Total"]["Orders"] = implement_reports.get(state).get(district).get("Total").get("Orders") or 0
        implement_reports[state][district]["Total"]["Hours"] = implement_reports.get(state).get(district).get("Total").get("Hours") + round(float(row["No of Hour"]), 2)
        implement_reports[state][district]["Total"]["Orders"] = implement_reports.get(state).get(district).get("Total").get("Orders") + 1


        implement_reports[state][district][hub] = implement_reports.get(state).get(district).get(hub) or {}
        implement_reports[state][district][hub]["Completed Hrs"] = implement_reports.get(state).get(district).get(hub).get("Completed Hrs") or 0
        implement_reports[state][district][hub]["Count"] = implement_reports.get(state).get(district).get(hub).get("Count") or 0

        # implement_reports[state][hub] = implement_reports.get(state).get(hub) or {}
        # implement_reports[state][hub]["Completed Hrs"] = implement_reports.get(state).get(hub).get("Completed Hrs") or 0
        # implement_reports[state][hub]["Count"] = implement_reports.get(state).get(hub).get("Count") or 0

        implement_reports[state][district][hub]["Completed Hrs"] = implement_reports.get(state).get(district).get(hub).get("Completed Hrs") + round(float(row["No of Hour"]), 2)
        implement_reports[state][district][hub]["Count"] = implement_reports.get(state).get(district).get(hub).get("Count") + 1
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
    district_index = first_row.index("Suplier District")
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
        dates.append((date.today() - timedelta(i)).strftime("%d/%m/%Y"))

    for state in implements_old_pf:
        implements[state] = implements.get(state) or {}
        if state != "Total":
            for district in implements_old_pf[state]:
                implements[state][district] = implements.get(state).get(district) or {}
                if district != "Total" and district != "C2Cs on New Platform":
                    for hub in implements_old_pf[state][district]:
                        if hub != "Total":    
                            implements[state][district][hub] = implements.get(state).get(district).get(hub) or {}
                            implements[state][district][hub]["Completed Hrs"] = implements.get(state).get(district).get(hub).get("Completed Hrs") or 0
                            implements[state][district][hub]["Count"] = implements.get(state).get(district).get(hub).get("Count")
                            implements[state][district][hub]["Completed Hrs"] = implements_old_pf.get(state).get(district).get(hub).get("Completed Hrs")
                            implements[state][district][hub]["Count"] = implements_old_pf.get(state).get(district).get(hub).get("Count")
                        elif hub == "Total":
                            implements[state][district]["Total"] = implements.get(state).get(district).get("Total") or {}
                            implements[state][district]["Total"]["Hours"] = implements.get(state).get(district).get("Total").get("Hours") or 0
                            implements[state][district]["Total"]["Orders"] = implements.get(state).get(district).get("Total").get("Orders") or 0
                            implements[state][district]["Total"]["Hours"] = implements_old_pf.get(state).get(district).get("Total").get("Hours")
                            implements[state][district]["Total"]["Orders"] = implements_old_pf.get(state).get(district).get("Total").get("Orders")
                elif district == "Total":
                    implements[state]["Total"] = implements.get(state).get("Total") or {}
                    implements[state]["Total"]["Hours"] = implements.get(state).get("Total").get("Hours") or 0
                    implements[state]["Total"]["Orders"] = implements.get(state).get("Total").get("Orders") or 0
                    implements[state]["Total"]["Hours"] = implements_old_pf.get(state).get("Total").get("Hours")
                    implements[state]["Total"]["Orders"] = implements_old_pf.get(state).get("Total").get("Orders")
                elif district == "C2Cs on New Platform":
                    implements[state]["C2Cs on New Platform"] = implements.get(state).get("C2Cs on New Platform") or {}
                    implements[state]["C2Cs on New Platform"]["Hours"] = implements.get(state).get("C2Cs on New Platform").get("Hours") or 0
                    implements[state]["C2Cs on New Platform"]["Orders"] = implements.get(state).get("C2Cs on New Platform").get("Orders") or 0
                    implements[state]["C2Cs on New Platform"]["Hours"] = implements_old_pf.get(state).get("C2Cs on New Platform").get("Hours")
                    implements[state]["C2Cs on New Platform"]["Orders"] = implements_old_pf.get(state).get("C2Cs on New Platform").get("Orders")

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
                district = "Gandhinagar".title()
            else:
                state = row[state_index].title() 
                district = row[district_index].title() 
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
            
            implements[state][district] = implements.get(state).get(district) or {}
            implements[state][district]["Total"] = implements.get(state).get(district).get("Total") or {}
            implements[state][district]["Total"]["Hours"] = implements.get(state).get(district).get("Total").get("Hours") or 0
            implements[state][district]["Total"]["Orders"] = implements.get(state).get(district).get("Total").get("Orders") or 0
            implements[state][district]["Total"]["Hours"] = implements.get(state).get(district).get("Total").get("Hours") + round(float(row[time_index])/60, 2)
            implements[state][district]["Total"]["Orders"] = implements.get(state).get(district).get("Total").get("Orders") + 1


            if row[hub_index] == "":
                implements[state]["C2Cs on New Platform"]["Hours"] = implements.get(state).get("C2Cs on New Platform").get("Hours") + round(float(row[time_index])/60, 2)
                implements[state]["C2Cs on New Platform"]["Orders"] = implements.get(state).get("C2Cs on New Platform").get("Orders") + 1    
            else:
                implements[state][district][row[hub_index]] = implements.get(state).get(district).get(row[hub_index]) or {}
                implements[state][district][row[hub_index]]["Completed Hrs"] = implements.get(state).get(district).get(row[hub_index]).get("Completed Hrs") or 0
                implements[state][district][row[hub_index]]["Count"] = implements.get(state).get(district).get(row[hub_index]).get("Count") or 0
                # implements[state][row[hub_index]] = implements.get(state).get(row[hub_index]) or {}
                # implements[state][row[hub_index]]["Completed Hrs"] = implements.get(state).get(row[hub_index]).get("Completed Hrs") or 0
                # implements[state][row[hub_index]]["Count"] = implements.get(state).get(row[hub_index]).get("Count") or 0

                if row[driver_type_index] == "HUB":
                    implements[state][district][row[hub_index]]["Completed Hrs"] = implements.get(state).get(district).get(row[hub_index]).get("Completed Hrs") + round(float(row[time_index])/60, 2)
                    implements[state][district][row[hub_index]]["Count"] = implements.get(state).get(district).get(row[hub_index]).get("Count") + 1

    implements["Total"] = implements.get("Total") or {}
    implements["Total"]["Hours"] = implements.get("Total").get("Hours") or 0
    implements["Total"]["Orders"] = implements.get("Total").get("Orders") or 0
    implements["Total"]["Hours"] = implements.get("Total").get("Hours") + implements_hours
    implements["Total"]["Orders"] = implements.get("Total").get("Orders") + implements_orders
    
    print("new pf implements =   " + format(implements_orders))
    print("new pf implement hours =   " + format(implements_hours))

    with open("final_implements.json" , 'w') as f:
        json.dump(implements, f)

    return implements