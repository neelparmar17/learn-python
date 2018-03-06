import csv
import json
from datetime import date, timedelta
from poc2 import transform_orders
# import subprocess 
# subprocess.call("./automate.sh")


def transform_data(file_name, yesterday):
    input_file = csv.DictReader(open(file_name))
    count_hours = 0
    count_orders = 0
    order_reports = {}

    for row in input_file:
        if (row["Status"] == "Completed"):
            order_reports[row["State"]] = order_reports.get(row["State"]) or {}
            order_reports[row["State"]]["Total"] = order_reports.get(row["State"]).get("Total") or {}
            order_reports[row["State"]]["Total"]["Hours"] = order_reports.get(row["State"]).get("Total").get("Hours") or 0
            order_reports[row["State"]]["Total"]["Hours"] = order_reports.get(row["State"]).get("Total").get("Hours") + round(float(row["Hours"]), 2)
            order_reports[row["State"]]["Total"]["Orders"] = order_reports.get(row["State"]).get("Total").get("Orders") or 0
            order_reports[row["State"]]["Total"]["Orders"] = order_reports.get(row["State"]).get("Total").get("Orders") + 1
            order_reports[row["State"]][row["Hub"]] = order_reports.get(row["State"]).get(row["Hub"]) or {}
            order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") or 0
            order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") or 0
            
            if row["Driver Type"] == "Franchisee":
                order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") + round(float(row["Hours"]), 2)

            count_orders += 1
            count_hours += round(float(row["Hours"]), 2)
            order_reports[row["State"]][row["Hub"]]["orders"] = (order_reports.get(row["State"]).get(row["Hub"]).get("orders")) or 0
            order_reports[row["State"]][row["Hub"]]["orders"] = (order_reports.get(row["State"]).get(row["Hub"]).get("orders")) + 1

    order_reports["Total"] = order_reports.get("Total") or {}
    order_reports["Total"]["Hours"] = order_reports.get("Total").get("Hours") or 0
    order_reports["Total"]["Orders"] = order_reports.get("Total").get("Orders") or 0
    order_reports["Total"]["Hours"] = round(order_reports.get("Total").get("Hours") + count_hours, 2)
    order_reports["Total"]["Orders"] = order_reports.get("Total").get("Orders") + count_orders
    print("total hours tractor + harvestor   ="+format(count_hours))
    print("total orders tractor + harvestor   =" + format(count_orders))
    with open("order_reports.json",  'w') as f:
        json.dump(order_reports, f)
    
    return order_reports


def transform_data_c2c_franchisee(file_name, yesterday):
    input_file = csv.DictReader(open(file_name))
    c2c_hours = 0
    Franchisee_hours = 0
    total = 0
    day_before_yesterday = date.today() - timedelta(2)
    order_reports = {}
    print("day before yesterday  " + format(day_before_yesterday))

    for row in input_file:
        if row["Status"] == "Completed" and row["Order Date"] == "04/03/2018":
            order_reports[row["State"]] = order_reports.get(row["State"]) or {}
            order_reports[row["State"]][row["Hub"]] = order_reports.get(row["State"]).get(row["Hub"]) or {}
            order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") or 0
            order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") or 0
            
            if row["Driver Type"] == "Franchisee":
                order_reports[row["State"]][row["Hub"]]["Franchisee"] = order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + round(float(row["Hours"]), 2)
            
            if row["Driver Type"] == "C2C":
                order_reports[row["State"]][row["Hub"]]["C2C"] = order_reports.get(row["State"]).get(row["Hub"]).get("C2C") + round(float(row["Hours"]), 2)

            order_reports[row["State"]][row["Hub"]]["Total"] = order_reports.get(row["State"]).get(row["Hub"]).get("Total") or 0
            order_reports[row["State"]][row["Hub"]]["Total"] = (round(order_reports.get(row["State"]).get(row["Hub"]).get("Franchisee") + order_reports.get(row["State"]).get(row["Hub"]).get("C2C"), 2))

    with open("c2c_franchinsee.json", 'w') as f:
        json.dump(order_reports, f)
    
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
            customer_reports[row["State"]][row["Hub"]]= customer_reports.get(row["State"]).get(row["Hub"]) or {}
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") or 0
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") + 1
            customer_count.append(row["Mobile"])
            count_total_customer += 1
    
    customer_reports["Total"] = customer_reports.get("Total") or {}
    customer_reports["Total"]["Count"] = count_total_customer
    s = set(customer_count)
    print("total farmers count   =   "+ format(len(s)))
    # print("Total registered farmers   =" + format(customer_count))
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
                if hub != "Total":
                    daily_report[state][hub] = daily_report.get(state).get(hub) or {}
                    daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {}
                    daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {"Count": 0}
                    daily_report[state][hub]["Implements only"]["Completed Hrs"] = implements[state][hub]["Completed Hrs"]
                    daily_report[state][hub]["Implements only"]["Count"] = implements[state][hub]["Count"]
                else:
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {"Count": 0}
                    daily_report[state]["Total"]["Implements only"]["Completed Hrs"] = round(implements[state]["Total"]["Hours"], 2)
                    daily_report[state]["Total"]["Implements only"]["Count"] = implements[state]["Total"]["Orders"]
        else:
            daily_report[state]["Implement Hours"] = implements[state]["Hours"]
            daily_report[state]["Implement Orders"] = implements[state]["Orders"]

    for state in customers:
        daily_report[state] = daily_report.get(state) or {}
        if state != "Total":
            for hub in customers[state]:
                if hub != "Total":
                    daily_report[state][hub] = daily_report.get(state).get(hub) or {}
                    daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {}
                    daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state][hub]["Registered Farmers"]["Count"] = customers[state][hub]["Count"]
                else:
                    daily_report[state]["Total"] = daily_report.get(state).get("Total") or {}
                    daily_report[state]["Total"]["Registered Farmers"] = daily_report.get(state).get("Total").get("Registered Farmers") or {}
                    daily_report[state]["Total"]["Implements only"] = daily_report.get(state).get("Total").get("Implements only") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Tractor+Harvestor"] = daily_report.get(state).get("Total").get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
                    daily_report[state]["Total"]["Registered Farmers"]["Count"] = customers[state]["Total"]["Count"]
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
    
    for state in c2c_franchinsee:
        c2c_franchinsee_report[state] = c2c_franchinsee_report.get(state) or {}

        for hub in c2c_franchinsee[state]:
            c2c_franchinsee_report[state][hub] = c2c_franchinsee_report.get(state).get(hub) or {}
            c2c_franchinsee_report[state][hub]["C2C"] = 0
            c2c_franchinsee_report[state][hub]["Franchisee"] = 0
            c2c_franchinsee_report[state][hub]["C2C"] = c2c_franchinsee_report[state][hub]["C2C"] + c2c_franchinsee[state][hub]["C2C"]
            c2c_franchinsee_report[state][hub]["Franchisee"] = c2c_franchinsee_report[state][hub]["Franchisee"] + c2c_franchinsee[state][hub]["Franchisee"]
            c2c_franchinsee_report[state][hub]["Total"] = c2c_franchinsee_report[state][hub]["Total"] + c2c_franchinsee[state][hub]["Total"]
    
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
               "orders hours": daily_report["Total"]["Order Hours"],
               "orders count": daily_report["Total"]["Order Count"],
               "implements hours": daily_report["Total"]["Implement Hours"],
               "implements count": daily_report["Total"]["Implement Orders"],
               "customer count": daily_report["Total"]["Customer Count"],
              }

    for state in daily_report:
        rowspan = format(len(daily_report[state].keys()))
        if state != "Total":
            email_html+= """
                <tr>
                    <td rowspan = %(rowspan)s>
                        %(state)s
                    </td>
                    <td>Total</td>
                    <td>%(orders hours)s</td>
                    <td>%(orders count)s</td>
                    <td>%(implement hours)s</td>
                    <td>%(implement count)s</td>
                    <td>%(customer count)s</td>
                    </tr>
            """ % {"rowspan": rowspan,
                "state": state,
                "orders hours": daily_report.get(state).get("Total").get("Tractor+Harvestor").get("Completed Hrs"),
                "orders count": daily_report.get(state).get("Total").get("Tractor+Harvestor").get("Count"),
                "implement hours": daily_report.get(state).get("Total").get("Implements only").get("Completed Hrs"),
                "implement count": daily_report.get(state).get("Total").get("Implements only").get("Count"),
                "customer count": daily_report.get(state).get("Total").get("Registered Farmers").get("Count"),
                }

            for hub in daily_report[state]:
                if hub != "Total":
                    email_html += """
                        <tr>
                            <td>
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
                            "tractor_hours": round(daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"], 0),
                            "tractor_orders": round(daily_report[state][hub]["Tractor+Harvestor"]["Count"], 0),
                            "implement_hours": round(daily_report[state][hub]["Implements only"]["Completed Hrs"], 0),
                            "implement_orders": round(daily_report[state][hub]["Implements only"]["Count"], 0),
                            "farmer_count": round(daily_report[state][hub]["Registered Farmers"]["Count"], 0),
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
    """ % {"before_yesterday": (date.today() - timedelta(2)).strftime("%d/%m/%Y"), "yesterday": yesterday.strftime("%d/%m/%Y")}
    for state in aggregate_c2c_franchisee:
        rowspan = format(len(aggregate_c2c_franchisee[state].keys()) + 1)
        report_html += """
        <tr>
            <td rowspan = %(rowspan)s>
                %(state)s
            </td>
        </tr>
        """  % {"rowspan": rowspan, "state": state}

        for hub in aggregate_c2c_franchisee[state]:
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

    report_html+="""
    </table>
    </body>
    </html>
    """

    return report_html

def generate_daily_report():
    yesterday = date.today() - timedelta(1)
    orders = transform_data("orders_report_temp.csv", yesterday)
    implements = transform_data_implement("implement_rented_report_temp.csv", yesterday)
    customers = transform_data_customer("customer_report_temp.csv", yesterday)
    c2c_franchinsee = transform_data_c2c_franchisee("orders_report_temp.csv", yesterday)
   
    aggregate_c2c_franchisee = aggregate_data_c2c_franchisee(c2c_franchinsee, orders)
    # print(aggregate_c2c_franchisee)
    # final_orders = transform_orders(orders, "orders.xlsx")
    # final_customers = transform_customers(customers, "orders.xlsx")

    daily_report = aggregate_data(orders, implements, customers)
    email_html = generate_html(daily_report, yesterday)
    report_html = generate_daily_report_html(aggregate_c2c_franchisee, email_html, yesterday, orders)
    with open("report.html", 'w') as html:
        html.write(email_html)
    
    with open("full_report.html", 'w') as full_html:
        full_html.write(report_html)
    
    return report_html


generate_daily_report()




