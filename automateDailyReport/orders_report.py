import csv
import json
from datetime import date, timedelta
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
        if row["Status"] == "Completed" and row["Order Date"] == "26/02/2018":
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
        implement_reports[row["State Name"]][row["Hub Name"]] = implement_reports.get(row["State Name"]).get(row["Hub Name"]) or {}
        implement_reports[row["State Name"]][row["Hub Name"]]["Completed Hrs"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Completed Hrs") or 0
        implement_reports[row["State Name"]][row["Hub Name"]]["Count"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Count") or 0

        implement_reports[row["State Name"]][row["Hub Name"]]["Completed Hrs"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Completed Hrs") + round(float(row["No of Hour"]), 2)
        implement_reports[row["State Name"]][row["Hub Name"]]["Count"] = implement_reports.get(row["State Name"]).get(row["Hub Name"]).get("Count") + 1
        count_hours += round(float(row["No of Hour"]), 2)
        count_orders += 1
    
    print("implement total hours    ="+format(count_hours))
    print("implement total orders   ="+format(count_orders))

    with open("implement_rented.json" , 'w') as f:
        json.dump(implement_reports, f)
    
    return implement_reports
        

def transform_data_customer(file_name, yesterday):
    input_csv = csv.DictReader(open(file_name))
    customer_reports = {}
    count_customer =0
    for row in input_csv:
        if row["Hub"] != "":
            customer_reports[row["State"]] = customer_reports.get(row["State"]) or {}
            customer_reports[row["State"]][row["Hub"]]= customer_reports.get(row["State"]).get(row["Hub"]) or {}
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") or 0
            customer_reports[row["State"]][row["Hub"]]["Count"] = customer_reports.get(row["State"]).get(row["Hub"]).get("Count") + 1
            count_customer += 1
    
    print("Total registered farmers   =" + format(count_customer))
    with open("customer_report.json" , 'w') as f:
        json.dump(customer_reports, f)

    return customer_reports

def aggregate_data(orders, implements, customers):
    daily_report = {}
    for state in orders:
        daily_report[state] = daily_report.get(state) or {}

        for hub in orders[state]:
            daily_report[state][hub] = daily_report.get(state).get(hub) or {}
            daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {}
            daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
            daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {"Count": 0}
            daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"] = round(orders[state][hub]["C2C"] + orders[state][hub]["Franchisee"], 2)
            daily_report[state][hub]["Tractor+Harvestor"]["Count"] = orders[state][hub]["orders"]

    for state in implements:
        daily_report[state] = daily_report.get(state) or {}

        for hub in implements[state]:
            daily_report[state][hub] = daily_report.get(state).get(hub) or {}
            daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {}
            daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
            daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {"Count": 0}
            daily_report[state][hub]["Implements only"]["Completed Hrs"] = implements[state][hub]["Completed Hrs"]
            daily_report[state][hub]["Implements only"]["Count"] = implements[state][hub]["Count"]

    for state in customers:
        daily_report[state] = daily_report.get(state) or {}

        for hub in customers[state]:
            daily_report[state][hub] = daily_report.get(state).get(hub) or {}
            daily_report[state][hub]["Registered Farmers"] = daily_report.get(state).get(hub).get("Registered Farmers") or {}
            daily_report[state][hub]["Implements only"] = daily_report.get(state).get(hub).get("Implements only") or {"Completed Hrs": 0, "Count": 0}
            daily_report[state][hub]["Tractor+Harvestor"] = daily_report.get(state).get(hub).get("Tractor+Harvestor") or {"Completed Hrs": 0, "Count": 0}
            daily_report[state][hub]["Registered Farmers"]["Count"] = customers[state][hub]["Count"]


    with open("daily_report.json", 'w') as f:
        json.dump(daily_report, f)

    return daily_report

def aggregate_data_c2c_franchisee(c2c_franchinsee):
    c2c_franchinsee_report = {}
    for state in c2c_franchinsee:
        c2c_franchinsee_report[state] = c2c_franchinsee_report.get(state) or {}

        for hub in c2c_franchinsee[state]:
            c2c_franchinsee_report[state][hub] = c2c_franchinsee_report.get(state).get(hub) or {}
            c2c_franchinsee_report[state][hub]["C2C"] = 0
            c2c_franchinsee_report[state][hub]["Franchisee"] = 0
            c2c_franchinsee_report[state][hub]["C2C"] = c2c_franchinsee[state][hub]["C2C"]
            c2c_franchinsee_report[state][hub]["Franchisee"] = c2c_franchinsee[state][hub]["Franchisee"]
            c2c_franchinsee_report[state][hub]["Total"] = c2c_franchinsee[state][hub]["Total"]
    
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
        <th colspan="5">%(date)s</th>
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
        </tr>""" % {"date": yesterday.strftime("%d/%m/%Y")}

    for state in daily_report:
        rowspan = format(len(daily_report[state].keys()) + 1)
        email_html+= """
            <tr>
                <td rowspan = %(rowspan)s>
                    %(state)s
                </td>
                </tr>
        """ % {"rowspan": rowspan, "state": state}


        for hub in daily_report[state]:
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
                    "tractor_hours": daily_report[state][hub]["Tractor+Harvestor"]["Completed Hrs"],
                    "tractor_orders": daily_report[state][hub]["Tractor+Harvestor"]["Count"],
                    "implement_hours": daily_report[state][hub]["Implements only"]["Completed Hrs"],
                    "implement_orders": daily_report[state][hub]["Implements only"]["Count"],
                    "farmer_count": daily_report[state][hub]["Registered Farmers"]["Count"],
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
        <th colspan="3">yesterday -1</th>
        <th colspan="3">MTD(yesterday)</th>
        </tr>
        <tr>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        </tr>
    """
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
                    "yesterday_c2c": round(aggregate_c2c_franchisee[state][hub]["C2C"], 2),
                    "yesterday_franchisee": round(aggregate_c2c_franchisee[state][hub]["Franchisee"], 2),
                    "yesterday_total": aggregate_c2c_franchisee[state][hub]["Total"],
                    "mtd_c2c": round(orders[state][hub]["C2C"], 2),
                    "mtd_franchisee": round(orders[state][hub]["Franchisee"], 2),
                    "mtd_total": round(orders[state][hub]["C2C"] + orders[state][hub]["Franchisee"], 2),
                  }

    report_html+="""
    </table>
    </body>
    </html>
    """

    return report_html

def generate_daily_report():
    yesterday = date.today() - timedelta(1)
    orders = transform_data("orders_report.csv", yesterday)
    implements = transform_data_implement("implement_rented_report.csv", yesterday)
    customers = transform_data_customer("customer_report.csv", yesterday)
    c2c_franchinsee = transform_data_c2c_franchisee("orders_report.csv", yesterday)
   
    aggregate_c2c_franchisee = aggregate_data_c2c_franchisee(c2c_franchinsee)
    print(aggregate_c2c_franchisee)
   
    daily_report = aggregate_data(orders, implements, customers)
    email_html = generate_html(daily_report, yesterday)
    report_html = generate_daily_report_html(aggregate_c2c_franchisee, email_html, yesterday, orders)
    with open("report.html", 'w') as html:
        html.write(email_html)
    
    with open("full_report.html", 'w') as full_html:
        full_html.write(report_html)
    
    return report_html


generate_daily_report()




