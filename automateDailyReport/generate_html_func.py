import csv
import json
from datetime import date, timedelta

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