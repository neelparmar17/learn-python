import pyexcel as pe
import csv
import json
from datetime import date, timedelta

def transform_data_c2c_franchisee(old_file_name, new_report, yesterday):
    input_file = csv.DictReader(open(old_file_name))
    
    sheet = pe.get_sheet(file_name=new_report)
    first_row = sheet.row_at(0)
    state_index = first_row.index("Suplier State")
    hub_index = first_row.index("Hub")
    order_date_index = first_row.index("Order Date")
    status_index = first_row.index("Status")
    driver_type_index = first_row.index("Driver Type")
    time_index = first_row.index("Minutes")
    sheet.name_columns_by_row(0)
    orders_count = 0
    hours_count = 0


    c2c_hours = 0
    Franchisee_hours = 0
    total = 0
    day_before_yesterday = (date.today() - timedelta(2)).strftime("%d/%m/%Y")
    order_reports = {}
    print("day before yesterday  " + format(day_before_yesterday))

    for row in input_file:
        state_name = row["State"]
        hub_name = row["Hub"]
        district = row["District"]
        if row["Status"] == "Completed" and row["Order Date"] == day_before_yesterday:
            order_reports[state_name] = order_reports.get(state_name) or {}
            
            
            order_reports[state_name][district] = order_reports.get(state_name).get(district) or {}

            order_reports[state_name][district][hub_name] = order_reports.get(state_name).get(district).get(hub_name) or {}
            order_reports[state_name][district][hub_name]["Franchisee"] = order_reports.get(state_name).get(district).get(hub_name).get("Franchisee") or 0
            order_reports[state_name][district][hub_name]["C2C"] = order_reports.get(state_name).get(district).get(hub_name).get("C2C") or 0
            
            order_reports[state_name][district]["Total"] = order_reports.get(state_name).get(district).get("Total") or {}
            order_reports[state_name][district]["Total"]["C2C"] = order_reports.get(state_name).get(district).get("Total").get("C2C") or 0
            order_reports[state_name][district]["Total"]["Franchisee"] = order_reports.get(state_name).get(district).get("Total").get("Franchisee") or 0
            order_reports[state_name][district]["Total"]["Total"] = order_reports.get(state_name).get(district).get("Total").get("Total") or 0

            order_reports[state_name]["Total"] = order_reports.get(state_name).get("Total") or {}
            order_reports[state_name]["Total"]["C2C"] = order_reports.get(state_name).get("Total").get("C2C") or 0
            order_reports[state_name]["Total"]["Franchisee"] = order_reports.get(state_name).get("Total").get("Franchisee") or 0
            order_reports[state_name]["Total"]["Total"] = order_reports.get(state_name).get("Total").get("Total") or 0
            
            order_reports[state_name]["C2Cs on New Platform"] = order_reports.get(state_name).get("C2Cs on New Platform") or {}
            order_reports[state_name]["C2Cs on New Platform"]["C2C"] = order_reports.get(state_name).get("C2Cs on New Platform").get("C2C") or 0
            order_reports[state_name]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(state_name).get("C2Cs on New Platform").get("Franchisee") or 0
            order_reports[state_name]["C2Cs on New Platform"]["Total"] = order_reports.get(state_name).get("C2Cs on New Platform").get("Total") or 0


            if row["Driver Type"] == "Franchisee":
                Franchisee_hours += round(float(row["Hours"]), 2)
                order_reports[state_name]["Total"]["Franchisee"] = order_reports.get(state_name).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[state_name][district][hub_name]["Franchisee"] = order_reports.get(state_name).get(district).get(hub_name).get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[state_name][district]["Total"]["Franchisee"] = order_reports.get(state_name).get(district).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                c2c_hours += round(float(row["Hours"]), 2)
                order_reports[state_name]["Total"]["C2C"] = order_reports.get(state_name).get("Total").get("C2C") + round(float(row["Hours"]), 2)
                order_reports[state_name][district][hub_name]["C2C"] = order_reports.get(state_name).get(district).get(hub_name).get("C2C") + round(float(row["Hours"]), 2)
                order_reports[state_name][district]["Total"]["C2C"] = order_reports.get(state_name).get(district).get("Total").get("C2C") + round(float(row["Hours"]), 2)

            total += round(float(row["Hours"]), 2)
            order_reports[state_name][district][hub_name]["Total"] = order_reports.get(state_name).get(district).get(hub_name).get("Total") or 0
            order_reports[state_name][district][hub_name]["Total"] = (round(order_reports.get(state_name).get(district).get(hub_name).get("Franchisee")
                + order_reports.get(state_name).get(district).get(hub_name).get("C2C"), 2))
            
            order_reports[state_name]["Total"]["Total"] = (order_reports.get(state_name).get("Total").get("C2C") 
                + order_reports.get(state_name).get("Total").get("Franchisee"))
            
            order_reports[state_name][district]["Total"]["Total"] = (order_reports.get(state_name).get(district).get("Total").get("Franchisee")
                + order_reports.get(state_name).get(district).get("Total").get("C2C"))

    print("old pf franchisee = " + format(Franchisee_hours))
    print("old pf total = " + format(total))
    new_franchisee = 0
    new_pf_total = 0
    for row in sheet:
        if (row[order_date_index] == day_before_yesterday and (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index] == "Partially Paid" or row[status_index] == "Work Completed"
         or row[status_index] == "Closed" or row[status_index] == "Feedback" or row[status_index] == "Work Started") and (row[time_index] != "" and (int(row[time_index]) > 9 and int(row[time_index])< 1200))):
            
            if row[hub_index] == "Dahegam" and row[state_index] == "india":
                state = row[first_row.index("Suplier District")].title()
                district = "Gandhinagar".title()
            else:
                state = row[state_index].title()
                district = row[first_row.index("Suplier District")].title()

            new_pf_total += round(row[time_index]/60, 2)
            total += round(row[time_index]/60, 2)
            order_reports[state] = order_reports.get(state) or {}
            order_reports[state]["Total"] = order_reports.get(state).get("Total") or {}
            order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") or 0
            order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") or 0
            order_reports[state]["Total"]["Total"] = order_reports.get(state).get("Total").get("Total") or 0
            order_reports[state]["C2Cs on New Platform"] = order_reports.get(state).get("C2Cs on New Platform") or {}
            order_reports[state]["C2Cs on New Platform"]["C2C"] = order_reports.get(state).get("C2Cs on New Platform").get("C2C") or 0
            order_reports[state]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(state).get("C2Cs on New Platform").get("Franchisee") or 0
            order_reports[state]["C2Cs on New Platform"]["Total"] = order_reports.get(state).get("C2Cs on New Platform").get("Total") or 0

            order_reports[state][district] = order_reports.get(state).get(district) or {}
            order_reports[state][district]["Total"] = order_reports.get(state).get(district).get("Total") or {}
            order_reports[state][district]["Total"]["C2C"] = order_reports.get(state).get(district).get("Total").get("C2C") or 0
            order_reports[state][district]["Total"]["Franchisee"] = order_reports.get(state).get(district).get("Total").get("Franchisee") or 0
            order_reports[state][district]["Total"]["Total"] = order_reports.get(state).get(district).get("Total").get("Total") or 0

            if not row[hub_index]:
                c2c_hours += round(row[time_index]/60, 2)
                order_reports[state]["C2Cs on New Platform"]["C2C"] = order_reports.get(state).get("C2Cs on New Platform").get("C2C") + round(row[time_index]/60, 2)
                order_reports[state]["C2Cs on New Platform"]["Total"] = (order_reports.get(state).get("C2Cs on New Platform").get("Total") 
                    + order_reports.get(state).get("C2Cs on New Platform").get("C2C") )
                order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)
                order_reports[state][district]["Total"]["C2C"] = order_reports.get(state).get(district).get("Total").get("C2C") + round(row[time_index]/60, 2)
            else:
                order_reports[state][district][row[hub_index]] = order_reports.get(state).get(district).get(row[hub_index]) or {}
                order_reports[state][district][row[hub_index]]["C2C"] = order_reports.get(state).get(district).get(row[hub_index]).get("C2C") or 0
                order_reports[state][district][row[hub_index]]["Franchisee"] = order_reports.get(state).get(district).get(row[hub_index]).get("Franchisee") or 0
                order_reports[state][district][row[hub_index]]["Total"] = order_reports.get(state).get(district).get(row[hub_index]).get("Total") or 0

                new_franchisee += row[time_index]
                if row[driver_type_index] == "HUB":
                    Franchisee_hours += round(row[time_index]/60, 2)
                    order_reports[state][district][row[hub_index]]["Franchisee"] = order_reports.get(state).get(district).get(row[hub_index]).get("Franchisee") + round(row[time_index]/60, 2)
                    order_reports[state][district]["Total"]["Franchisee"] = order_reports.get(state).get(district).get("Total").get("Franchisee") + round(row[time_index]/60, 2)
                    order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") + round(row[time_index]/60, 2)
                elif row[driver_type_index] == "C2C":
                    c2c_hours += round(row[time_index]/60, 2)
                    order_reports[state][district][row[hub_index]]["C2C"] = order_reports.get(state).get(district).get(row[hub_index]).get("C2C") + round(row[time_index]/60, 2)
                    order_reports[state][district]["Total"]["C2C"] = order_reports.get(state).get(district).get("Total").get("C2C") + round(row[time_index]/60, 2)
                    order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)

                order_reports[state][district][row[hub_index]]["Total"] = (order_reports.get(state).get(district).get(row[hub_index]).get("Franchisee") 
                    + order_reports.get(state).get(district).get(row[hub_index]).get("C2C"))

                order_reports[state][district]["Total"]["Total"] = (order_reports.get(state).get(district).get("Total").get("C2C")
                    + order_reports.get(state).get(district).get("Total").get("Franchisee"))

            order_reports[state]["Total"]["Total"] = (order_reports.get(state).get("Total").get("Franchisee")
                + order_reports.get(state).get("Total").get("C2C")
                + order_reports.get(state).get("C2Cs on New Platform").get("Total")) 
    
    print("new pf franchisee = " + format(new_franchisee))
    print("NEW PF TOTAL = " + format(new_pf_total))
    print("total c2c" + format(c2c_hours))
    print("total franchisee" + format(Franchisee_hours))
    print("total of total" + format(total))

    order_reports["Total"] = order_reports.get("Total") or {}
    order_reports["Total"]["C2C"] = order_reports.get("Total").get("C2C") or 0
    order_reports["Total"]["Franchisee"] = order_reports.get("Total").get("Franchisee") or 0
    order_reports["Total"]["C2C"] = round(order_reports.get("Total").get("C2C") + c2c_hours, 2)
    order_reports["Total"]["Franchisee"] = round(order_reports.get("Total").get("Franchisee") + Franchisee_hours, 2)
    order_reports["Total"]["Total"] = round(total, 2)
    
    with open("c2c_franchinsee.json", 'w') as f:
        json.dump(order_reports, f)
    
    # print(order_reports)
    return order_reports
