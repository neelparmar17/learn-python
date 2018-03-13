import csv
import json
from datetime import date, timedelta


def aggregate_data(orders, implements, customers):
    daily_report = {}
    for state in orders:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for district in orders[state]:
                daily_report[state][district] = daily_report.get(state).get(district) or {}
                if district != "Total" and district != "C2Cs on New Platform":
                    for hub in orders[state][district]:
                        if hub != "Total":
                            daily_report[state][district][hub] = daily_report.get(state).get(district).get(hub) or {}
                            daily_report[state][district][hub]["Tractor+Harvestor"] = daily_report.get(state).get(district).get(hub).get("Tractor+Harvestor") or {}
                            daily_report[state][district][hub]["Implements only"] = daily_report.get(state).get(district).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district][hub]["Registered Farmers"] = daily_report.get(state).get(district).get(hub).get("Registered Farmers") or {"Count": 0}
                            daily_report[state][district][hub]["Tractor+Harvestor"]["Completed Hrs"] = round(orders[state][district][hub]["C2C"] + orders[state][district][hub]["Franchisee"], 2)
                            daily_report[state][district][hub]["Tractor+Harvestor"]["Count"] = orders[state][district][hub]["orders"]
                        if hub == "Total":
                            daily_report[state][district]["Total"] = daily_report.get(state).get(district).get("Total") or {}
                            daily_report[state][district]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get(district).get("Total").get("Tractor+Harvestor") or {}
                            daily_report[state][district]["Total"]["Implements only"] = daily_report.get(state).get(district).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district]["Total"]["Registered Farmers"] = daily_report.get(state).get(district).get("Total").get("Registered Farmers") or {"Count": 0}
                            daily_report[state][district]["Total"]["Tractor+Harvestor"]["Completed Hrs"] = round(orders[state][district]["Total"]["Hours"], 2)
                            daily_report[state][district]["Total"]["Tractor+Harvestor"]["Count"] = orders[state][district]["Total"]["Orders"]
                elif district=="Total":
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["Total"]["Tractor+Harvestor"]["Completed Hrs"] = round(orders.get(state).get("Total").get("Hours"), 2)
                    daily_report[state]["Total"]["Tractor+Harvestor"]["Count"] = orders.get(state).get("Total").get("Orders")
                elif district == "C2Cs on New Platform":
                    daily_report[state]["C2Cs on New Platform"] = daily_report.get(state).get("C2Cs on New Platform") or {}
                    daily_report[state]["C2Cs on New Platform"]["Tractor+Harvestor"] = daily_report.get(state).get("C2Cs on New Platform").get("Tractor+Harvestor") or {}
                    daily_report[state]["C2Cs on New Platform"]["Implements only"] = daily_report.get(state).get("C2Cs on New Platform").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Registered Farmers"] = daily_report.get(state).get("C2Cs on New Platform").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["C2Cs on New Platform"]["Tractor+Harvestor"]["Completed Hrs"] = round(orders[state]["C2Cs on New Platform"]["C2C"] + orders[state]["C2Cs on New Platform"]["Franchisee"], 2)
                    daily_report[state]["C2Cs on New Platform"]["Tractor+Harvestor"]["Count"] = orders[state]["C2Cs on New Platform"]["orders"]

        else:
            daily_report[state]["Order Hours"] = orders[state]["Hours"]
            daily_report[state]["Order Count"] = orders[state]["Orders"]

  
    for state in implements:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for district in implements[state]:
                daily_report[state][district] = daily_report.get(state).get(district) or {}
                if district != "Total" and district != "C2Cs on New Platform":
                    for hub in implements[state][district]:
                        if hub != "Total":
                            daily_report[state][district][hub] = daily_report.get(state).get(district).get(hub) or {}
                            daily_report[state][district][hub]["Implements only"] = daily_report.get(state).get(district).get(hub).get("Implements only") or {}
                            daily_report[state][district][hub]["Tractor+Harvestor"] = daily_report.get(state).get(district).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district][hub]["Registered Farmers"] = daily_report.get(state).get(district).get(hub).get("Registered Farmers") or {"Count": 0}
                            daily_report[state][district][hub]["Implements only"]["Completed Hrs"] = implements[state][district][hub]["Completed Hrs"]
                            daily_report[state][district][hub]["Implements only"]["Count"] = implements[state][district][hub]["Count"]
                        elif hub == "Total":
                            daily_report[state][district]["Total"] = daily_report.get(state).get(district).get("Total") or {}
                            daily_report[state][district]["Total"]["Implements only"] = daily_report.get(state).get(district).get("Total").get("Implements only") or {}
                            daily_report[state][district]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get(district).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district]["Total"]["Registered Farmers"] = daily_report.get(state).get(district).get("Total").get("Registered Farmers") or {"Count": 0}
                            daily_report[state][district]["Total"]["Implements only"]["Completed Hrs"] = round(implements[state][district]["Total"]["Hours"], 2)
                            daily_report[state][district]["Total"]["Implements only"]["Count"] = implements[state][district]["Total"]["Orders"]        
                elif district == "Total":
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["Total"]["Implements only"]["Completed Hrs"] = round(implements[state]["Total"]["Hours"], 2)
                    daily_report[state]["Total"]["Implements only"]["Count"] = implements[state]["Total"]["Orders"]
                elif district == "C2Cs on New Platform":
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
            for district in customers[state]:
                daily_report[state][district] = daily_report.get(state).get(district) or {}
                if district != "Total" and district != "C2Cs on New Platform":
                    for hub in customers[state][district]:
                        if hub != "Total":
                            daily_report[state][district][hub] = daily_report.get(state).get(district).get(hub) or {}
                            daily_report[state][district][hub]["Registered Farmers"] = daily_report.get(state).get(district).get(hub).get("Registered Farmers") or {}
                            daily_report[state][district][hub]["Implements only"] = daily_report.get(state).get(district).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district][hub]["Tractor+Harvestor"] = daily_report.get(state).get(district).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district][hub]["Registered Farmers"]["Count"] = customers[state][district][hub]["Count"]
                        elif hub == "Total":
                            daily_report[state][district]["Total"] = daily_report.get(state).get(district).get("Total") or {}
                            daily_report[state][district]["Total"]["Registered Farmers"] = daily_report.get(state).get(district).get("Total").get("Registered Farmers") or {}
                            daily_report[state][district]["Total"]["Implements only"] = daily_report.get(state).get(district).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get(district).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                            daily_report[state][district]["Total"]["Registered Farmers"]["Count"] = customers[state][district]["Total"]["Count"]
                elif district == "Total":
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"]["Count"] = customers[state]["Total"]["Count"]
                elif district == "C2Cs on New Platform":
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
