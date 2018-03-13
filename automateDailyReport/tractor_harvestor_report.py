import pyexcel as pe
import csv
import json
from datetime import date, timedelta

def transform_data(file_name, yesterday):
    input_file = csv.DictReader(open(file_name))
    count_hours = 0
    count_orders = 0
    order_reports = {}
    c2c_hours = 0
    Franchisee_hours = 0

    for row in input_file:
        state = row["State"]
        hub = row["Hub"]
        district = row["District"]
        if (row["Status"] == "Completed"):
            order_reports[state] = order_reports.get(state) or {}
            
            order_reports[state]["Total"] = order_reports.get(state).get("Total") or {}
            order_reports[state]["Total"]["Hours"] = order_reports.get(state).get("Total").get("Hours") or 0
            order_reports[state]["Total"]["Hours"] = order_reports.get(state).get("Total").get("Hours") + round(float(row["Hours"]), 2)
            order_reports[state]["Total"]["Orders"] = order_reports.get(state).get("Total").get("Orders") or 0
            order_reports[state]["Total"]["Orders"] = order_reports.get(state).get("Total").get("Orders") + 1
            order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") or 0
            order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") or 0

            order_reports[state]["C2Cs on New Platform"] = order_reports.get(state).get("C2Cs on New Platform") or {}
            order_reports[state]["C2Cs on New Platform"]["C2C"] = order_reports.get(state).get("C2Cs on New Platform").get("C2C") or 0
            order_reports[state]["C2Cs on New Platform"]["Franchisee"] = order_reports.get(state).get("C2Cs on New Platform").get("Franchisee") or 0
            order_reports[state]["C2Cs on New Platform"]["orders"] = order_reports.get(state).get("C2Cs on New Platform").get("orders") or 0

            order_reports[state][district] = order_reports.get(state).get(district) or {}
            order_reports[state][district][hub] = order_reports.get(state).get(district).get(hub) or {}
            order_reports[state][district][hub]["C2C"] = order_reports.get(state).get(district).get(hub).get("C2C") or 0
            order_reports[state][district][hub]["Franchisee"] = order_reports.get(state).get(district).get(hub).get("Franchisee") or 0


            order_reports[state][district]["Total"] = order_reports.get(state).get(district).get("Total") or {}
            order_reports[state][district]["Total"]["C2C"] = order_reports.get(state).get(district).get("Total").get("C2C") or 0
            order_reports[state][district]["Total"]["Franchisee"] = order_reports.get(state).get(district).get("Total").get("Franchisee") or 0
            order_reports[state][district]["Total"]["Hours"] = order_reports.get(state).get(district).get("Total").get("Hours") or 0
            order_reports[state][district]["Total"]["Orders"] = order_reports.get(state).get(district).get("Total").get("Orders") or 0
            # order_reports[state][hub] = order_reports.get(state).get(hub) or {}
            # order_reports[state][hub]["Franchisee"] = order_reports.get(state).get(hub).get("Franchisee") or 0
            # order_reports[state][hub]["C2C"] = order_reports.get(state).get(hub).get("C2C") or 0
            
            if row["Driver Type"] == "Franchisee":
                Franchisee_hours += round(float(row["Hours"]), 2)
                order_reports[state][district][hub]["Franchisee"] = order_reports.get(state).get(district).get(hub).get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["Franchisee"] = order_reports.get(state).get(district).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["Hours"] = order_reports.get(state).get(district).get("Total").get("Hours") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["Orders"] = order_reports.get(state).get(district).get("Total").get("Orders") + 1
                order_reports[state]["Total"]["Franchisee"] = order_reports.get(state).get("Total").get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                c2c_hours += round(float(row["Hours"]), 2)
                order_reports[state][district][hub]["C2C"] = order_reports.get(state).get(district).get(hub).get("C2C") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["C2C"] = order_reports.get(state).get(district).get("Total").get("C2C") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["Hours"] = order_reports.get(state).get(district).get("Total").get("Hours") + round(float(row["Hours"]), 2)
                order_reports[state][district]["Total"]["Orders"] = order_reports.get(state).get(district).get("Total").get("Orders") + 1
                order_reports[state]["Total"]["C2C"] = order_reports.get(state).get("Total").get("C2C") + round(float(row["Hours"]), 2)

            count_orders += 1
            count_hours += round(float(row["Hours"]), 2)
            order_reports[state][district][hub]["orders"] = (order_reports.get(state).get(district).get(hub).get("orders")) or 0
            order_reports[state][district][hub]["orders"] = (order_reports.get(state).get(district).get(hub).get("orders")) + 1

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


def transform_orders(orders_old_pf, fname):
    orders = {}
    sheet = pe.get_sheet(file_name=fname)
    first_row = sheet.row_at(0)
    state_index = first_row.index("Suplier State")
    district_index = first_row.index("Suplier District")
    hub_index = first_row.index("Hub")
    order_date_index = first_row.index("Order Date")
    status_index = first_row.index("Status")
    driver_type_index = first_row.index("Driver Type")
    time_index = first_row.index("Minutes")
    sku_index = first_row.index("sku_repr")
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
            for district in orders_old_pf[state]:
                orders[state][district] = orders.get(state).get(district) or {}
                if district != "Total" and district != "C2Cs on New Platform":
                    for hub in orders_old_pf[state][district]:
                        if hub != "Total":
                            orders[state][district][hub] = orders.get(state).get(district).get(hub) or {}
                            orders[state][district][hub]["Franchisee"] = orders.get(state).get(district).get(hub).get("Franchisee") or 0
                            orders[state][district][hub]["C2C"] = orders.get(state).get(district).get(hub).get("C2C") or 0
                            orders[state][district][hub]["orders"] = orders.get(state).get(district).get(hub).get("orders") or 0
                            orders[state][district][hub]["Franchisee"] = orders_old_pf.get(state).get(district).get(hub).get("Franchisee")
                            orders[state][district][hub]["C2C"] = orders_old_pf.get(state).get(district).get(hub).get("C2C")
                            orders[state][district][hub]["orders"] = orders_old_pf.get(state).get(district).get(hub).get("orders")
                        elif hub == "Total":
                            orders[state][district]["Total"] = orders.get(state).get(district).get("Total") or {}
                            orders[state][district]["Total"]["Franchisee"] = orders_old_pf.get(state).get(district).get("Total").get("Franchisee") or 0
                            orders[state][district]["Total"]["C2C"] = orders_old_pf.get(state).get(district).get("Total").get("C2C") or 0
                            orders[state][district]["Total"]["Orders"] = orders_old_pf.get(state).get(district).get("Total").get("Orders")
                            orders[state][district]["Total"]["Hours"] = orders_old_pf.get(state).get(district).get("Total").get("Hours")        
                elif district == "Total":
                    orders[state][district] = orders.get(state).get(district) or {}
                    orders[state][district]["Franchisee"] = orders_old_pf.get(state).get(district).get("Franchisee") or 0
                    orders[state][district]["C2C"] = orders_old_pf.get(state).get(district).get("C2C") or 0
                    orders[state][district]["Orders"] = orders_old_pf.get(state).get(district).get("Orders")
                    orders[state][district]["Hours"] = orders_old_pf.get(state).get(district).get("Hours")
                elif district == "C2Cs on New Platform":
                    orders[state][district] = orders.get(state).get(district) or {}
                    orders[state][district]["Franchisee"] = orders.get(state).get(district).get("Franchisee") or 0
                    orders[state][district]["C2C"] = orders.get(state).get(district).get("C2C") or 0
                    orders[state][district]["orders"] = orders.get(state).get(district).get("orders") or 0
                    orders[state][district]["Franchisee"] = orders_old_pf.get(state).get(district).get("Franchisee")
                    orders[state][district]["C2C"] = orders_old_pf.get(state).get(district).get("C2C")
                    orders[state][district]["orders"] = orders_old_pf.get(state).get(district).get("orders")
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
         or row[status_index] == "Closed" or row[status_index] == "Feedback" or row[status_index] == "Work Started") and (row[time_index] != "" and (int(row[time_index]) > 9 and int(row[time_index])< 1200)) and (row[sku_index] != "" and row[sku_index][-1] == "0"):
            
            if row[hub_index] == "Dahegam" and row[state_index] == "india":
                state = row[first_row.index("Suplier District")].title()
                district = "Gandhinagar".title()
            else:
                state = row[state_index].title()
                district = row[district_index].title() 
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

            orders[state][district] = orders.get(state).get(district) or {}

            orders[state][district]["Total"] = orders.get(state).get(district).get("Total") or {}
            orders[state][district]["Total"]["C2C"] = orders.get(state).get(district).get("Total").get("C2C") or 0
            orders[state][district]["Total"]["Franchisee"] = orders.get(state).get(district).get("Total").get("Franchisee") or 0
            orders[state][district]["Total"]["Hours"] = orders.get(state).get(district).get("Total").get("Hours") or 0
            orders[state][district]["Total"]["Orders"] = orders.get(state).get(district).get("Total").get("Orders") or 0
            orders[state][district]["Total"]["Hours"] = orders.get(state).get(district).get("Total").get("Hours") + round(int(row[time_index])/60, 2)
            orders[state][district]["Total"]["Orders"] = orders.get(state).get(district).get("Total").get("Orders") + 1



            if row[hub_index] == "":
                c2c_hours += round(row[time_index]/60, 2)
                orders[state]["C2Cs on New Platform"]["C2C"] = orders.get(state).get("C2Cs on New Platform").get("C2C") + round(row[time_index]/60, 2)
                orders[state][district]["Total"]["C2C"] = orders.get(state).get(district).get("Total").get("C2C") + round(row[time_index]/60, 2)

                orders[state]["C2Cs on New Platform"]["orders"] = orders.get(state).get("C2Cs on New Platform").get("orders") + 1
                orders[state]["Total"]["C2C"] = orders.get(state).get("Total").get("C2C") + round(row[time_index]/60, 2)
            else:
                orders[state][district][row[hub_index]] = orders.get(state).get(district).get(row[hub_index]) or {}
                orders[state][district][row[hub_index]]["C2C"] = orders.get(state).get(district).get(row[hub_index]).get("C2C") or 0
                orders[state][district][row[hub_index]]["Franchisee"] = orders.get(state).get(district).get(row[hub_index]).get("Franchisee") or 0
                orders[state][district][row[hub_index]]["orders"] = orders.get(state).get(district).get(row[hub_index]).get("orders") or 0
                # orders[state][row[hub_index]] = orders.get(state).get(row[hub_index]) or {}
                # orders[state][row[hub_index]]["C2C"] = orders.get(state).get(row[hub_index]).get("C2C") or 0
                # orders[state][row[hub_index]]["Franchisee"] = orders.get(state).get(row[hub_index]).get("Franchisee") or 0
            
                if row[driver_type_index] == "HUB":
                    Franchisee_hours += round(row[time_index]/60, 2)
                    orders[state][district][row[hub_index]]["Franchisee"] = orders.get(state).get(district).get(row[hub_index]).get("Franchisee") + round(row[time_index]/60, 2)
                    orders[state][district]["Total"]["Franchisee"] = orders.get(state).get(district).get("Total").get("Franchisee") + round(row[time_index]/60, 2)
                elif row[driver_type_index] == "C2C":
                    c2c_hours += round(row[time_index]/60, 2)
                    orders[state][district][row[hub_index]]["C2C"] = orders.get(state).get(district).get(row[hub_index]).get("C2C") + round(row[time_index]/60, 2)
                    orders[state][district]["Total"]["C2C"] = orders.get(state).get(district).get("Total").get("C2C") + round(row[time_index]/60, 2)
                
                orders[state][district][row[hub_index]]["orders"] = orders.get(state).get(district).get(row[hub_index]).get("orders") + 1
    
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
