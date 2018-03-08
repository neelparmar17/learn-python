import csv
import json
from datetime import date, timedelta
import pyexcel as pe
# import subprocess 

def transform_data(file_name, yesterday):
    input_file = csv.DictReader(open(file_name))
    count_hours = 0
    count_orders = 0
    order_reports = {}
    c2c_hours = 0
    Franchisee_hours = 0

    for row in input_file:
        if (row["Status"] == "Completed"):
            order_reports[row["State"]] = order_reports.get(row["State"]) or {}
            
            order_reports[row["State"]]["Total"] = order_reports.get(row["State"]).get("Total") or {}
            order_reports[row["State"]]["Total"]["Hours"] = order_reports.get(row["State"]).get("Total").get("Hours") or 0
            order_reports[row["State"]]["Total"]["Hours"] = order_reports.get(row["State"]).get("Total").get("Hours") + round(float(row["Hours"]), 2)
            order_reports[row["State"]]["Total"]["Orders"] = order_reports.get(row["State"]).get("Total").get("Orders") or 0
            order_reports[row["State"]]["Total"]["Orders"] = order_reports.get(row["State"]).get("Total").get("Orders") + 1
            order_reports[row["State"]]["Total"]["C2C"] = order_reports.get(row["State"]).get("Total").get("C2C") or 0
            order_reports[row["State"]]["Total"]["Franchisee"] = order_reports.get(row["State"]).get("Total").get("Franchisee") or 0

            order_reports[row["State"]]["C2Cs on New Platform"] = order_reports.get(row["State"]).get("C2Cs on New Platform") or {}
            order_reports[row["State"]]["C2Cs on New Platform"]["C2C"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("C2C") or 0
            order_reports[row["State"]]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("Franchisee") or 0
            order_reports[row["State"]]["C2Cs on New Platform"]["orders"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("orders") or 0

            order_reports[row["State"]][row["Hub"]] = order_reports.get(row["State"]).get(row["Hub"]) or {}
            order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") or 0
            order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") or 0
            
            if row["Driver Type"] == "Franchisee":
                Franchisee_hours += round(float(row["Hours"]), 2)
                order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[row["State"]]["Total"]["Franchisee"] = order_reports.get(row["State"]).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                c2c_hours += round(float(row["Hours"]), 2)
                order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") + round(float(row["Hours"]), 2)
                order_reports[row["State"]]["Total"]["C2C"] = order_reports.get(row["State"]).get("Total").get("C2C") + round(float(row["Hours"]), 2)

            count_orders += 1
            count_hours += round(float(row["Hours"]), 2)
            order_reports[row["State"]][row["Hub"]]["orders"] = (order_reports.get(row["State"]).get(row["Hub"]).get("orders")) or 0
            order_reports[row["State"]][row["Hub"]]["orders"] = (order_reports.get(row["State"]).get(row["Hub"]).get("orders")) + 1

    order_reports["Total"] = order_reports.get("Total") or {}
    order_reports["Total"]["Hours"] = order_reports.get("Total").get("Hours") or 0
    order_reports["Total"]["Orders"] = order_reports.get("Total").get("Orders") or 0
    order_reports["Total"]["Hours"] = round(order_reports.get("Total").get("Hours") + count_hours, 2)
    order_reports["Total"]["Orders"] = order_reports.get("Total").get("Orders") + count_orders
    order_reports["Total"]["C2C"] = c2c_hours
    order_reports["Total"]["Franchisee"] = Franchisee_hours
    
    print("total hours tractor + harvestor   ="+format(count_hours))
    print("total orders tractor + harvestor   =" + format(count_orders))
    
    with open("order_reports.json",  'w') as f:
        json.dump(order_reports, f)
    
    return order_reports


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
        if row["Status"] == "Completed" and row["Order Date"] == day_before_yesterday:
            order_reports[row["State"]] = order_reports.get(row["State"]) or {}
            order_reports[row["State"]][row["Hub"]] = order_reports.get(row["State"]).get(row["Hub"]) or {}
            order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") or 0
            order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") or 0
            order_reports[row["State"]]["Total"] = order_reports.get(row["State"]).get("Total") or {}
            order_reports[row["State"]]["Total"]["C2C"] = order_reports.get(row["State"]).get("Total").get("C2C") or 0
            order_reports[row["State"]]["Total"]["Franchisee"] = order_reports.get(row["State"]).get("Total").get("Franchisee") or 0
            order_reports[row["State"]]["Total"]["Total"] = order_reports.get(row["State"]).get("Total").get("Total") or 0
            
            order_reports[row["State"]]["C2Cs on New Platform"] = order_reports.get(row["State"]).get("C2Cs on New Platform") or {}
            order_reports[row["State"]]["C2Cs on New Platform"]["C2C"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("C2C") or 0
            order_reports[row["State"]]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("Franchisee") or 0
            order_reports[row["State"]]["C2Cs on New Platform"]["Total"] = order_reports.get(row["State"]).get("C2Cs on New Platform").get("Total") or 0

            if row["Driver Type"] == "Franchisee":
                Franchisee_hours += round(float(row["Hours"]), 2)
                order_reports[row["State"]]["Total"]["Franchisee"] = order_reports.get(row["State"]).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                c2c_hours += round(float(row["Hours"]), 2)
                order_reports[row["State"]]["Total"]["C2C"] = order_reports.get(row["State"]).get("Total").get("C2C") + round(float(row["Hours"]), 2)
                order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") + round(float(row["Hours"]), 2)
            total += round(float(row["Hours"]), 2)
            order_reports[row["State"]][row["Hub"]]["Total"] = order_reports.get(row["State"]).get(row["Hub"]).get("Total") or 0
            order_reports[row["State"]][row["Hub"]]["Total"] = (round(order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + order_reports.get(row["State"]).get(row["Hub"]).get("C2C"), 2))
            order_reports[row["State"]]["Total"]["Total"] = (order_reports.get(row["State"]).get("Total").get("C2C") 
                + order_reports.get(row["State"]).get("Total").get("Franchisee"))

    print("old pf franchisee = " + format(Franchisee_hours))
    print("old pf total = " + format(total))
    new_franchisee = 0
    new_pf_total = 0
    for row in sheet:
        if (row[order_date_index] == day_before_yesterday and (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index] == "Partially Paid" or row[status_index] == "Work Completed"
         or row[status_index] == "Closed" or row[status_index] == "Feedback" or row[status_index] == "Work Started") and (row[time_index] != "" and (int(row[time_index]) > 9 and int(row[time_index])< 1200))):
            
            if row[hub_index] == "Dahegam" and row[state_index] == "india":
                state = row[first_row.index("Suplier District")].title()
            else:
                state = row[state_index].title() 
            new_pf_total += round(row[time_index]/60, 2)
            total += round(row[time_index]/60, 2)
            order_reports[state] = order_reports.get(state) or {}
            order_reports[state]["Total"] = order_reports.get(state).get("Total") or {}
            order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") or 0
            order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") or 0
            order_reports[state]["Total"]["Total"] = order_reports.get(state).get("Total").get("Total") or 0

            if not row[hub_index]:
                c2c_hours += round(row[time_index]/60, 2)
                order_reports[state]["C2Cs on New Platform"] = order_reports.get(state).get("C2Cs on New Platform") or {}
                order_reports[state]["C2Cs on New Platform"]["C2C"] = order_reports.get(state).get("C2Cs on New Platform").get("C2C") or 0
                order_reports[state]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(state).get("C2Cs on New Platform").get("Franchisee") or 0
                order_reports[state]["C2Cs on New Platform"]["C2C"] = order_reports.get(state).get("C2Cs on New Platform").get("C2C") + round(row[time_index]/60, 2)
                order_reports[state]["C2Cs on New Platform"]["Total"] = order_reports.get(state).get("C2Cs on New Platform").get("Total") or 0
                order_reports[state]["C2Cs on New Platform"]["Total"] = order_reports.get(state).get("C2Cs on New Platform").get("Total") + order_reports.get(state).get("C2Cs on New Platform").get("C2C") 
                order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)
            else:
                order_reports[state][row[hub_index]] = order_reports.get(state).get(row[hub_index]) or {}
                order_reports[state][row[hub_index]]["C2C"] = order_reports.get(state).get(row[hub_index]).get("C2C") or 0
                order_reports[state][row[hub_index]]["Franchisee"] = order_reports.get(state).get(row[hub_index]).get("Franchisee") or 0
                order_reports[state][row[hub_index]]["Total"] = order_reports.get(state).get(row[hub_index]).get("Total") or 0

                new_franchisee += row[time_index]
                if row[driver_type_index] == "HUB":
                    Franchisee_hours += round(row[time_index]/60, 2)
                    order_reports[state][row[hub_index]]["Franchisee"] = order_reports.get(state).get(row[hub_index]).get("Franchisee") + round(row[time_index]/60, 2)
                    order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") + round(row[time_index]/60, 2)
                elif row[driver_type_index] == "C2C":
                    c2c_hours += round(row[time_index]/60, 2)
                    order_reports[state][row[hub_index]]["C2C"] = order_reports.get(state).get(row[hub_index]).get("C2C") + round(row[time_index]/60, 2)
                    order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)

                order_reports[state][row[hub_index]]["Total"] = order_reports.get(state).get(row[hub_index]).get("Franchisee") + order_reports.get(state).get(row[hub_index]).get("C2C")
            
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
        

def transform_data_customer(file_name, yesterday):
    input_csv = csv.DictReader(open(file_name))
    customer_reports = {}
    customer_count = []
    count_total_customer =0
    for row in input_csv:
        if row["Hub"] != "":
            customer_reports[row["State"]] = customer_reports.get(row["State"]) or {}
            
            customer_reports[row["State"]]["Total"] = customer_reports.get(row["State"]).get("Total") or {}
            customer_reports[row["State"]]["Total"]["Count"] = customer_reports.get(row["State"]).get("Total").get("Count") or 0
            customer_reports[row["State"]]["Total"]["Count"] = customer_reports.get(row["State"]).get("Total").get("Count") + 1

            customer_reports[row["State"]]["C2Cs on New Platform"] = customer_reports.get(row["State"]).get("C2Cs on New Platform") or {}
            customer_reports[row["State"]]["C2Cs on New Platform"]["Count"] = customer_reports.get(row["State"]).get("C2Cs on New Platform").get("Count") or 0
            
            customer_reports[row["State"]][row["Hub"]]= customer_reports.get(row["State"]).get(row["Hub"]) or {}
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") or 0
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") + 1
            customer_count.append(row["Mobile"])
            count_total_customer += 1
    
    customer_reports["Total"] = customer_reports.get("Total") or {}
    customer_reports["Total"]["Count"] = count_total_customer
    s = set(customer_count)
    print("total farmers count   =   "+ format(len(s)))
    
    with open("customer_report.json" , 'w') as f:
        json.dump(customer_reports, f)

    return customer_reports

def aggregate_data(orders, implements, customers):
    daily_report = {}
    for state in orders:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for hub in orders[state]:
                if hub != "Total":
                    daily_report[state][hub] = daily_report.get(state).get(hub) or {}
                    daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {}
                    daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {"Count": 0}
                    daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"] = round(orders[state][hub]["C2C"] + orders[state][hub]["Franchisee"], 2)
                    daily_report[state][hub]["Tractor+Harvestor"]["Count"] = orders[state][hub]["orders"]
                else:
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["Total"]["Tractor+Harvestor"]["Completed Hrs"] = round(orders.get(state).get("Total").get("Hours"), 2)
                    daily_report[state]["Total"]["Tractor+Harvestor"]["Count"] = orders.get(state).get("Total").get("Orders")
        else:
            daily_report[state]["Order Hours"] = orders[state]["Hours"]
            daily_report[state]["Order Count"] = orders[state]["Orders"]

    for state in implements:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for hub in implements[state]:
                if hub != "Total" and hub != "C2Cs on New Platform":
                    daily_report[state][hub] = daily_report.get(state).get(hub) or {}
                    daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {}
                    daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {"Count": 0}
                    daily_report[state][hub]["Implements only"]["Completed Hrs"] = implements[state][hub]["Completed Hrs"]
                    daily_report[state][hub]["Implements only"]["Count"] = implements[state][hub]["Count"]
                elif hub == "Total":
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["Total"]["Implements only"]["Completed Hrs"] = round(implements[state]["Total"]["Hours"], 2)
                    daily_report[state]["Total"]["Implements only"]["Count"] = implements[state]["Total"]["Orders"]
                elif hub == "C2Cs on New Platform":
                    daily_report[state]["C2Cs on New Platform"] = daily_report.get(state).get("C2Cs on New Platform") or {}
                    daily_report[state]["C2Cs on New Platform"]["Implements only"] = daily_report.get(state).get("C2Cs on New Platform").get("Implements only") or {}
                    daily_report[state]["C2Cs on New Platform"]["Tractor+Harvestor"] = daily_report.get(state).get("C2Cs on New Platform").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Registered Farmers"] = daily_report.get(state).get("C2Cs on New Platform").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Implements only"]["Completed Hrs"] = round(implements[state]["C2Cs on New Platform"]["Hours"], 2)
                    daily_report[state]["C2Cs on New Platform"]["Implements only"]["Count"] = implements[state]["C2Cs on New Platform"]["Orders"]
        else:
            daily_report[state]["Implement Hours"] = implements[state]["Hours"]
            daily_report[state]["Implement Orders"] = implements[state]["Orders"]

    for state in customers:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for hub in customers[state]:
                if hub != "Total" and hub != "C2Cs on New Platform":
                    daily_report[state][hub] = daily_report.get(state).get(hub) or {}
                    daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {}
                    daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Registered Farmers"]["Count"] = customers[state][hub]["Count"]
                elif hub == "Total":
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"]["Count"] = customers[state]["Total"]["Count"]
                elif hub == "C2Cs on New Platform":
                    daily_report[state]["C2Cs on New Platform"] = daily_report.get(state).get("C2Cs on New Platform") or {}
                    daily_report[state]["C2Cs on New Platform"]["Registered Farmers"] = daily_report.get(state).get("C2Cs on New Platform").get("Registered Farmers") or {}
                    daily_report[state]["C2Cs on New Platform"]["Implements only"] = daily_report.get(state).get("C2Cs on New Platform").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Tractor+Harvestor"] = daily_report.get(state).get("C2Cs on New Platform").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Registered Farmers"]["Count"] = customers[state]["C2Cs on New Platform"]["Count"]
        else:
            daily_report[state]["Customer Count"] = customers[state]["Count"]


    with open("daily_report.json", 'w') as f:
        json.dump(daily_report, f)

    return daily_report

def aggregate_data_c2c_franchisee(c2c_franchinsee, orders):
    c2c_franchinsee_report = {}
    for state in orders:
        if state != "Total":
            c2c_franchinsee_report[state] = c2c_franchinsee_report.get(state) or {}
            for hub in orders[state]:
                if hub != "Total":
                    c2c_franchinsee_report[state][hub] = c2c_franchinsee_report.get(state).get(hub) or {}
                    c2c_franchinsee_report[state][hub] = c2c_franchinsee_report.get(state).get(hub) or {}
                    c2c_franchinsee_report[state][hub]["C2C"] = 0
                    c2c_franchinsee_report[state][hub]["Franchisee"] = 0
                    c2c_franchinsee_report[state][hub]["Total"] = 0
                else:
                    c2c_franchinsee_report[state]["Total"] = c2c_franchinsee_report.get(state).get("Total") or {}
                    c2c_franchinsee_report[state]["Total"]["C2C"] = c2c_franchinsee_report.get(state).get("Total").get("C2C") or 0
                    c2c_franchinsee_report[state]["Total"]["Franchisee"] = c2c_franchinsee_report.get(state).get("Total").get("Franchisee") or 0
                    c2c_franchinsee_report[state]["Total"]["Total"] = c2c_franchinsee_report.get(state).get("Total").get("Total") or 0
    
    for state in c2c_franchinsee:
        if state != "Total":
            c2c_franchinsee_report[state] = c2c_franchinsee_report.get(state) or {}
            for hub in c2c_franchinsee[state]:
                if hub != "Total":
                    c2c_franchinsee_report[state][hub] = c2c_franchinsee_report.get(state).get(hub) or {}
                    c2c_franchinsee_report[state][hub]["C2C"] = 0
                    c2c_franchinsee_report[state][hub]["Franchisee"] = 0
                    c2c_franchinsee_report[state][hub]["C2C"] = c2c_franchinsee_report[state][hub]["C2C"] + c2c_franchinsee[state][hub]["C2C"]
                    c2c_franchinsee_report[state][hub]["Franchisee"] = c2c_franchinsee_report[state][hub]["Franchisee"] + c2c_franchinsee[state][hub]["Franchisee"]
                    c2c_franchinsee_report[state][hub]["Total"] = c2c_franchinsee_report[state][hub]["Total"] + c2c_franchinsee[state][hub]["Total"]
                else:
                    c2c_franchinsee_report[state]["Total"] = c2c_franchinsee_report.get(state).get("Total") or {}
                    c2c_franchinsee_report[state]["Total"]["C2C"] = c2c_franchinsee.get(state).get("Total").get("C2C")
                    c2c_franchinsee_report[state]["Total"]["Franchisee"] = c2c_franchinsee.get(state).get("Total").get("Franchisee")
                    c2c_franchinsee_report[state]["Total"]["Total"] = c2c_franchinsee.get(state).get("Total").get("Total")
        else:
            c2c_franchinsee_report["Total"] = c2c_franchinsee_report.get("Total") or {}
            c2c_franchinsee_report["Total"]["C2C"] = c2c_franchinsee.get("Total").get("C2C")
            c2c_franchinsee_report["Total"]["Franchisee"] = c2c_franchinsee.get("Total").get("Franchisee")
            c2c_franchinsee_report["Total"]["Total"] = c2c_franchinsee.get("Total").get("Total")
   
    with open("final_c2c_franchisee.json", 'w') as f:
        json.dump(c2c_franchinsee_report, f)
    return c2c_franchinsee_report

def generate_html(daily_report, yesterday):
    email_html = """<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: center;    
        }
        </style>
    <title>Document</title>
    </head>
    <body>
    <table>
        <tr>
        <th rowspan="3">State</th>
        <th rowspan="3">Hub</th>
        <th colspan="5">MTD(%(date)s)</th>
        </tr>
        <tr>
        <th colspan="2">Tractor+Harvestor</th>
        <th colspan="2">Implement only</th>
        <th colspan="1">Registered farmers</th>
        </tr>
        <tr>
        <td>completed Hrs</td>
        <td>count</td>
        <td>completed Hrs</td>
        <td>count</td>
        <td>count</td>
        </tr>
        <tr>
        <td>Total</td>
        <td></td>
        <td>%(orders hours)s</td>
        <td>%(orders count)s</td>
        <td>%(implements hours)s</td>
        <td>%(implements count)s</td>
        <td>%(customer count)s</td>
        </tr>
        """ % {"date": yesterday.strftime("%d/%m/%Y"),
               "orders hours": round(daily_report["Total"]["Order Hours"], 0),
               "orders count": round(daily_report["Total"]["Order Count"], 0),
               "implements hours": round(daily_report["Total"]["Implement Hours"], 0),
               "implements count": round(daily_report["Total"]["Implement Orders"], 0),
               "customer count": round(daily_report["Total"]["Customer Count"], 0),
              }

    for state in daily_report:
        rowspan = format(len(daily_report[state].keys()))
        if state != "Total":
            email_html+= """
                <tr>
                    <td rowspan = %(rowspan)s>
                        %(state)s
                    </td>
                    <td bgcolor = %(color)s>Total</td>
                    <td bgcolor = %(color)s>%(orders hours)s</td>
                    <td bgcolor = %(color)s>%(orders count)s</td>
                    <td bgcolor = %(color)s>%(implement hours)s</td>
                    <td bgcolor = %(color)s>%(implement count)s</td>
                    <td bgcolor = %(color)s>%(customer count)s</td>
                    </tr>
            """ % {"rowspan": rowspan,
                "state": state,
                "color": "#fbf193",
                "orders hours": round(daily_report.get(state).get("Total").get("Tractor+Harvestor").get("Completed Hrs"), 0),
                "orders count": round(daily_report.get(state).get("Total").get("Tractor+Harvestor").get("Count"), 0),
                "implement hours": round(daily_report.get(state).get("Total").get("Implements only").get("Completed Hrs"), 0),
                "implement count": round(daily_report.get(state).get("Total").get("Implements only").get("Count"), 0),
                "customer count": round(daily_report.get(state).get("Total").get("Registered Farmers").get("Count"), 0),
                }

            for hub in daily_report[state]:
                if hub != "Total" and hub != "C2Cs on New Platform":
                    email_html += """
                        <tr>
                            <td bgcolor= "%(color)s">
                                %(hub)s
                            </td>
                            <td>
                                %(tractor_hours)s
                            </td>
                            <td>
                                %(tractor_orders)s
                            </td>
                            <td>
                                %(implement_hours)s
                            </td>
                            <td>
                                %(implement_orders)s
                            </td>
                            <td>
                                %(farmer_count)s
                            </td>

                        </tr>
                    """ % { "hub": hub,
                            "color": "#fb9393" if (daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"] == 0 and daily_report[state][hub]["Implements only"]["Completed Hrs"] == 0 and daily_report[state][hub]["Tractor+Harvestor"]["Count"] == 0 and daily_report[state][hub]["Implements only"]["Count"] == 0) else "#ffffff",
                            "tractor_hours": round(daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"], 0),
                            "tractor_orders": round(daily_report[state][hub]["Tractor+Harvestor"]["Count"], 0),
                            "implement_hours": round(daily_report[state][hub]["Implements only"]["Completed Hrs"], 0),
                            "implement_orders": round(daily_report[state][hub]["Implements only"]["Count"], 0),
                            "farmer_count": round(daily_report[state][hub]["Registered Farmers"]["Count"], 0),
                        }
            print(state)
            email_html += """
                <tr bgcolor = %(color)s>
                    <td>%(c2c_new)s</td>
                    <td>%(tractor_hours)s</td>
                    <td>%(tractor_orders)s</td>
                    <td>%(implement_hours)s</td>
                    <td>%(implement_orders)s</td>
                    <td>%(farmer_count)s</td>
                </tr>
            """  % { "c2c_new": "C2Cs on New Platform",
                     "color": "#9bc4ff",
                     "tractor_hours": round(daily_report.get(state).get("C2Cs on New Platform").get("Tractor+Harvestor").get("Completed Hrs"), 0),
                     "tractor_orders": round(daily_report.get(state).get("C2Cs on New Platform").get("Tractor+Harvestor").get("Count"), 0),
                     "implement_hours": round(daily_report.get(state).get("C2Cs on New Platform").get("Implements only").get("Completed Hrs"), 0),
                     "implement_orders": round(daily_report.get(state).get("C2Cs on New Platform").get("Implements only").get("Count"), 0),
                     "farmer_count": round(daily_report.get(state).get("C2Cs on New Platform").get("Registered Farmers").get("Count"), 0),
                    }

    email_html += """</table>
    """
    
    return email_html

def generate_daily_report_html(aggregate_c2c_franchisee, email_html, yesterday, orders):
    report_html = email_html + """
    <br>
    <br>
    <br>
    <table>
        <tr>
        <th rowspan="2">State</th>
        <th rowspan="2">Hub</th>
        <th colspan="3">%(before_yesterday)s</th>
        <th colspan="3">MTD(%(yesterday)s)</th>
        </tr>
        <tr>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        </tr>
        <tr>
        <td>Total</td>
        <td></td>
        <td>%(yesterday_c2c)s</td>
        <td>%(yesterday_franchisee)s</td>
        <td>%(yesterday_total)s</td>
        <td>%(mtd_c2c)s</td>
        <td>%(mtd_franchisee)s</td>
        <td>%(mtd_total)s</td>
        </tr>
    """ % {"before_yesterday": (date.today() - timedelta(2)).strftime("%d/%m/%Y"),
           "yesterday": yesterday.strftime("%d/%m/%Y"),
           "yesterday_c2c": round(aggregate_c2c_franchisee.get("Total").get("C2C"), 0),
           "yesterday_franchisee": round(aggregate_c2c_franchisee.get("Total").get("Franchisee"), 0),
           "yesterday_total": round(aggregate_c2c_franchisee.get("Total").get("Total"), 0),
           "mtd_c2c": round(orders.get("Total").get("C2C"),0),
           "mtd_franchisee": round(orders.get("Total").get("Franchisee"), 0),
           "mtd_total": round(orders.get("Total").get("Hours"), 0),
          }
    for state in aggregate_c2c_franchisee:
        rowspan = format(len(aggregate_c2c_franchisee[state].keys()))
        if state != "Total":
            report_html += """
            <tr>
                <td rowspan = %(rowspan)s>
                    %(state)s
                </td>
                <td bgcolor = %(color)s>Total</td>
                <td bgcolor = %(color)s>%(yesterday_c2c)s</td>
                <td bgcolor = %(color)s>%(yesterday_franchisee)s</td>
                <td bgcolor = %(color)s>%(yesterday_total)s</td>
                <td bgcolor = %(color)s>%(mtd_c2c)s</td>
                <td bgcolor = %(color)s>%(mtd_franchisee)s</td>
                <td bgcolor = %(color)s>%(mtd_total)s</td>
            </tr>
            """  % {"rowspan": rowspan,
                    "state": state,
                    "color": "#fbf193",
                    "yesterday_c2c": round(aggregate_c2c_franchisee.get(state).get("Total").get("C2C"),0),
                    "yesterday_franchisee": round(aggregate_c2c_franchisee.get(state).get("Total").get("Franchisee"), 0),
                    "yesterday_total": round(aggregate_c2c_franchisee.get(state).get("Total").get("Total") or 0, 0),
                    "mtd_c2c": round(orders.get(state).get("Total").get("C2C") or 0, 0),
                    "mtd_franchisee": round(orders.get(state).get("Total").get("Franchisee") or 0, 0),
                    "mtd_total": round(orders.get(state).get("Total").get("Hours") or 0, 0),
                   }

            for hub in aggregate_c2c_franchisee[state]:
                if hub != "Total" and hub != "C2Cs on New Platform":
                    report_html+="""
                    <tr>
                        <td>%(hub)s</td>
                        <td>%(yesterday_c2c)s</td>
                        <td>%(yesterday_franchisee)s</td>
                        <td>%(yesterday_total)s</td>
                        <td>%(mtd_c2c)s</td>
                        <td>%(mtd_franchisee)s</td>
                        <td>%(mtd_total)s</td>
                    </tr>
                    """ % { "hub": hub,
                            "yesterday_c2c": round(aggregate_c2c_franchisee[state][hub]["C2C"], 0),
                            "yesterday_franchisee": round(aggregate_c2c_franchisee[state][hub]["Franchisee"],0),
                            "yesterday_total": round(aggregate_c2c_franchisee[state][hub]["Total"], 0),
                            "mtd_c2c": round(orders.get(state).get(hub).get("C2C"), 0),
                            "mtd_franchisee": round(orders[state][hub]["Franchisee"], 0),
                            "mtd_total": round(orders[state][hub]["C2C"] + orders[state][hub]["Franchisee"], 0),
                        }
            report_html+= """
                <tr bgcolor = "%(color)s">
                    <td>%(c2cs_new)s</td>
                    <td>%(yesterday_c2c)s</td>
                    <td>%(yesterday_franchisee)s</td>
                    <td>%(yesterday_total)s</td>
                    <td>%(mtd_c2c)s</td>
                    <td>%(mtd_franchisee)s</td>
                    <td>%(mtd_total)s</td>
                </tr>
            """  % { "c2cs_new": "C2Cs on New Platform",
                     "color" : "#9bc4ff",
                     "yesterday_c2c": round(aggregate_c2c_franchisee[state]["C2Cs on New Platform"]["C2C"], 0),
                     "yesterday_franchisee": round(aggregate_c2c_franchisee[state]["C2Cs on New Platform"]["Franchisee"],0),
                     "yesterday_total": round(aggregate_c2c_franchisee[state]["C2Cs on New Platform"]["Total"], 0),
                     "mtd_c2c": round(orders.get(state).get("C2Cs on New Platform").get("C2C"), 0),
                     "mtd_franchisee": round(orders[state]["C2Cs on New Platform"]["Franchisee"], 0),
                     "mtd_total": round(orders[state]["C2Cs on New Platform"]["C2C"] + orders[state]["C2Cs on New Platform"]["Franchisee"], 0),
                   }

    report_html+="""
    </table>
    </body>
    </html>
    """

    return report_html

def transform_orders(orders_old_pf, fname):
    orders = {}
    sheet = pe.get_sheet(file_name=fname)
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

    today = date.today()
    yesterday = date.today() - timedelta(1)
    print(yesterday)
    yesterday_date = int(yesterday.strftime("%d"))
    # dates = ["01/03/2018", "02/03/2018", "03/03/2018", "04/03/2018"]
    dates = []

    for state in orders_old_pf:
        orders[state] = orders.get(state) or {}
        if state != "Total":
            for hub in orders_old_pf[state]:
                if hub != "Total":
                    orders[state][hub] = orders.get(state).get(hub) or {}
                    orders[state][hub]["Franchisee"] = orders.get(state).get(hub).get("Franchisee") or 0
                    orders[state][hub]["C2C"] = orders.get(state).get(hub).get("C2C") or 0
                    orders[state][hub]["orders"] = orders.get(state).get(hub).get("orders") or 0
                    orders[state][hub]["Franchisee"] = orders_old_pf.get(state).get(hub).get("Franchisee")
                    orders[state][hub]["C2C"] = orders_old_pf.get(state).get(hub).get("C2C")
                    orders[state][hub]["orders"] = orders_old_pf.get(state).get(hub).get("orders")
                else:
                    orders[state][hub] = orders.get(state).get(hub) or {}
                    orders[state][hub]["Franchisee"] = orders_old_pf.get(state).get(hub).get("Franchisee") or 0
                    orders[state][hub]["C2C"] = orders_old_pf.get(state).get(hub).get("C2C") or 0
                    orders[state][hub]["Orders"] = orders_old_pf.get(state).get(hub).get("Orders")
                    orders[state][hub]["Hours"] = orders_old_pf.get(state).get(hub).get("Hours")
        else:
            orders["Total"] = orders.get("Total") or {}
            orders["Total"]["Franchisee"] = orders_old_pf.get("Total").get("Franchisee")
            orders["Total"]["C2C"] = orders_old_pf.get("Total").get("C2C")
            orders["Total"]["Hours"] = orders_old_pf.get("Total").get("Hours")
            orders["Total"]["Orders"] = orders_old_pf.get("Total").get("Orders")

    for i in range(1, yesterday_date+1):
        print(i)
        dates.append((date.today() - timedelta(i)).strftime("%d/%m/%Y"))

    print(dates)
    for row in sheet:
        if (yesterday.strftime("%m/%Y") in row[order_date_index] and row[order_date_index] in dates) and (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index] == "Partially Paid" or row[status_index] == "Work Completed"
         or row[status_index] == "Closed" or row[status_index] == "Feedback" or row[status_index] == "Work Started") and (row[time_index] != "" and (int(row[time_index]) > 9 and int(row[time_index])< 1200)):
            
            if row[hub_index] == "Dahegam" and row[state_index] == "india":
                state = row[first_row.index("Suplier District")].title()
            else:
                state = row[state_index].title() 
            orders[state] = orders.get(state) or {}
            orders_count += 1
            hours_count += round(round(float(row[time_index]/60), 2), 2)
            
            orders[state]["Total"] = orders.get(state).get("Total") or {}
            orders[state]["Total"]["Hours"] = orders.get(state).get("Total").get("Hours") or 0
            orders[state]["Total"]["Orders"] = orders.get(state).get("Total").get("Orders") or 0
            orders[state]["Total"]["Hours"] = orders.get(state).get("Total").get("Hours") + round(int(row[time_index])/60, 2)
            orders[state]["Total"]["Orders"] = orders.get(state).get("Total").get("Orders") + 1
            orders[state]["Total"]["Franchisee"] = orders.get(state).get("Total").get("Franchisee") or 0
            orders[state]["Total"]["C2C"] = orders.get(state).get("Total").get("C2C") or 0
           
            orders[state]["C2Cs on New Platform"] = orders.get(state).get("C2Cs on New Platform") or {}
            orders[state]["C2Cs on New Platform"]["Franchisee"] = orders.get(state).get("C2Cs on New Platform").get("Franchisee") or 0
            orders[state]["C2Cs on New Platform"]["C2C"] = orders.get(state).get("C2Cs on New Platform").get("C2C") or 0
            orders[state]["C2Cs on New Platform"]["orders"] = orders.get(state).get("C2Cs on New Platform").get("orders") or 0
            
            if row[hub_index] == "":
                c2c_hours += round(row[time_index]/60, 2)
                orders[state]["C2Cs on New Platform"]["C2C"] = orders.get(state).get("C2Cs on New Platform").get("C2C") + round(row[time_index]/60, 2)
                orders[state]["C2Cs on New Platform"]["orders"] = orders.get(state).get("C2Cs on New Platform").get("orders") + 1
                orders[state]["Total"]["C2C"] = orders.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)
            else:
                orders[state][row[hub_index]] = orders.get(state).get(row[hub_index]) or {}
                orders[state][row[hub_index]]["C2C"] = orders.get(state).get(row[hub_index]).get("C2C") or 0
                orders[state][row[hub_index]]["Franchisee"] = orders.get(state).get(row[hub_index]).get("Franchisee") or 0
            
                if row[driver_type_index] == "HUB":
                    Franchisee_hours += round(row[time_index]/60, 2)
                    orders[state][row[hub_index]]["Franchisee"] = orders.get(state).get(row[hub_index]).get("Franchisee") + round(row[time_index]/60, 2)
                    orders[state]["Total"]["Franchisee"] = orders.get(state).get("Total").get("Franchisee") + round(row[time_index]/60, 2)
                elif row[driver_type_index] == "C2C":
                    c2c_hours += round(row[time_index]/60, 2)
                    orders[state][row[hub_index]]["C2C"] = orders.get(state).get(row[hub_index]).get("C2C") + round(row[time_index]/60, 2)
            
                orders[state][row[hub_index]]["orders"] = orders.get(state).get(row[hub_index]).get("orders") or 0
                orders[state][row[hub_index]]["orders"] = orders.get(state).get(row[hub_index]).get("orders") + 1
    
    orders["Total"] = orders.get("Total") or {}
    orders["Total"]["Hours"] = orders.get("Total").get("Hours") or 0
    orders["Total"]["Hours"] = round(orders.get("Total").get("Hours") + hours_count, 2)
    orders["Total"]["Orders"] = orders.get("Total").get("Orders") or 0
    orders["Total"]["Orders"] = orders.get("Total").get("Orders") + orders_count
    orders["Total"]["C2C"] = orders.get("Total").get("C2C") + round(c2c_hours, 2)
    orders["Total"]["Franchisee"] = orders.get("Total").get("Franchisee") + round(Franchisee_hours, 2)
    
    print("new pf orders  =" + format(orders_count))
    print("new pf hours = " + format(hours_count))
    
    with open("final_orders.json", 'w') as f:
        json.dump(orders, f)
    
    return orders

def generate_daily_report():
    # subprocess.call("./automate.sh")
    yesterday = date.today() - timedelta(1)
    
    orders = transform_data("Order_Report_08Mar18.csv", yesterday)
    implements = transform_data_implement("'Implement_Report_08Mar18'.csv", yesterday)
    customers = transform_data_customer("'Customer_Report_08Mar18'.csv", yesterday)
    c2c_franchinsee = transform_data_c2c_franchisee("Order_Report_08Mar18.csv", "OrdersNewPF.XLSX", yesterday)
    final_orders = transform_orders(orders,   "OrdersNewPF.XLSX")
    
    aggregate_daily_report = aggregate_data(final_orders, implements, customers)
    aggregate_c2c_franchisee = aggregate_data_c2c_franchisee(c2c_franchinsee, final_orders)

    email_html = generate_html(aggregate_daily_report, yesterday)
    report_html = generate_daily_report_html(aggregate_c2c_franchisee, email_html, yesterday, final_orders)
    with open("report.html", 'w') as html:
        html.write(email_html)
    
    with open("full_report.html", 'w') as full_html:
        full_html.write(report_html)
    
    return report_html


generate_daily_report()