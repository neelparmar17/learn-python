from datetime import date, timedelta
import json
# print(sheet.column["Order Date"])

def transform_orders(orders, fname):
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
    today = date.today()
    yesterday = date.today() - timedelta(1)
    yesterday_date = int(yesterday.strftime("%d"))
    print(yesterday_date)
    dates = []
    for i in range(1, yesterday_date+1):
        dates.append((date.today() - timedelta(i)).strftime("%d/%m/%Y"))
    
    print(dates)
    for row in sheet:
        if (yesterday.strftime("%m/%Y") in row[order_date_index] and row[order_date_index] in dates) and (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index] == "Partially Paid" or row[status_index] == "Work Completed"
         or row[state_index] == "Closed" or row[status_index] == "Feedback" or row[state_index] == "Work Started") and (row[time_index] > 9 and row[time_index]< 1200):
            if row[hub_index] == "Dahegam":
                state = row[first_row.index("Suplier District")].title()
            else:
                state = row[state_index].title() 
            orders[state] = orders.get(state) or {}
            orders_count += 1
            hours_count += round(round(float(row[time_index]/60), 2), 2)
            
            orders[state]["Total"] = orders.get(state).get("Total") or {}
            orders[state]["Total"]["Hours"] = orders.get(state).get("Total").get("Hours") or 0
            orders[state]["Total"]["Orders"] = orders.get(state).get("Total").get("Orders") or 0
            orders[state]["Total"]["Hours"] = orders.get(state).get("Total").get("Hours") + round(row[time_index]/60, 2)
            orders[state]["Total"]["Orders"] = orders.get(state).get("Total").get("Orders") + 1
            
            if row[hub_index] == "":
                orders[state]["new C2C orders"] = orders.get(state).get("new C2C orders") or {}
                orders[state]["new C2C orders"]["Franchisee"] = orders.get(state).get("new C2C orders").get("Franchisee") or 0
                orders[state]["new C2C orders"]["C2C"] = orders.get(state).get("new C2C orders").get("C2C") or 0
                orders[state]["new C2C orders"]["C2C"] = orders.get(state).get("new C2C orders").get("C2C") + round(row[time_index]/60, 2)
                orders[state]["new C2C orders"]["orders"] = orders.get(state).get("new C2C orders").get("orders") or 0
                orders[state]["new C2C orders"]["orders"] = orders.get(state).get("new C2C orders").get("orders") + 1
            else:
                # if row[hub_index]== "Dahegam":
                #     state = row[first_row.index("Suplier District")].title()
                # if row[hub_index] != "Dahegam":
                orders[state][row[hub_index]] = orders.get(state).get(row[hub_index]) or {}
                orders[state][row[hub_index]]["C2C"] = orders.get(state).get(row[hub_index]).get("C2C") or 0
                orders[state][row[hub_index]]["Franchisee"] = orders.get(state).get(row[hub_index]).get("Franchisee") or 0
                if row[driver_type_index] == "HUB":
                    orders[state][row[hub_index]]["Franchisee"] = orders.get(state).get(row[hub_index]).get("Franchisee") + round(row[time_index]/60, 2)
                elif row[driver_type_index] == "C2C":
                    orders[state][row[hub_index]]["C2C"] = orders.get(state).get(row[hub_index]).get("C2C") + round(row[time_index]/60, 2)
                orders[state][row[hub_index]]["orders"] = orders.get(state).get(row[hub_index]).get("orders") or 0
                orders[state][row[hub_index]]["orders"] = orders.get(state).get(row[hub_index]).get("orders") + 1

    
    orders["Total"] = orders.get("Total") or {}
    orders["Total"]["Hours"] = orders.get("Total").get("Hours") or 0
    orders["Total"]["Hours"] = round(orders.get("Total").get("Hours") + hours_count, 2)
    orders["Total"]["Orders"] = orders.get("Total").get("Orders") or 0
    orders["Total"]["Orders"] = orders.get("Total").get("Orders") + orders_count
    print("new pf orders  =" + format(orders_count))
    print("new pf hours = " + format(hours_count))
    with open("final_orders.json", 'w') as f:
        json.dump(orders, f)
    
    return orders

# def transform_customers(customer_report, fname):
#     sheet = pe.get_sheet(file_name=fname)
#     first_row = sheet.row_at(0)
#     old_order_index = first_row.index("old_order_id")
#     state_index = first_row.index("Customer State")
#     hub_index = first_row.index("Hub")
#     status_index = first_row.index("Status")
#     driver_type_index = first_row.index("Driver Type")
#     order_date_index = first_row.index("Order Date")
#     sheet.name_columns_by_row(0)
#     new_pf_count = 0
#     for row in sheet:
#         if (row[status_index] == "Payment Completed" or row[status_index] == "Order Completed" or row[status_index]=="Work Completed") and ("02/2018" in row[order_date_index] and row[order_date_index]!= "28/02/2018") and (row[old_order_index] == ""):
#             state = row[state_index].title() 
#             new_pf_count += 1 
#             customer_report[state] = customer_report.get(state) or {}
#             if row[hub_index] == "":
#                 customer_report[state]["C2Cs on new platform"] = customer_report.get(state).get("C2Cs on new platform") or {}
#                 customer_report[state]["C2Cs on new platform"]["Count"] = customer_report.get(state).get("C2Cs on new platform").get("Count") or 0
#                 customer_report[state]["C2Cs on new platform"]["Count"] = customer_report.get(state).get("C2Cs on new platform").get("Count") + 1
#             else:
#                 customer_report[state][row[hub_index]] = customer_report.get(state).get(row[hub_index]) or {}
#                 customer_report[state][row[hub_index]]["Count"] = customer_report.get(state).get(row[hub_index]).get("Count") or 0
#                 customer_report[state][row[hub_index]]["Count"] = customer_report.get(state).get(row[hub_index]).get("Count") + 1
    
#     with open("final_customers.json", 'w') as f:
#         print("new pf count = " + format(new_pf_count))
#         json.dump(customer_report, f)
    
#     return customer_report