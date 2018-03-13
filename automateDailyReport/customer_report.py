import csv
import json
from datetime import date, timedelta

def transform_data_customer(file_name, yesterday):
    input_csv = csv.DictReader(open(file_name))
    customer_reports = {}
    customer_count = []
    count_total_customer =0
    for row in input_csv:
        state = row["State"]
        hub = row["Hub"]
        district = row["District"]
        if hub != "":
            customer_reports[state] = customer_reports.get(state) or {}
            
            customer_reports[state]["Total"] = customer_reports.get(state).get("Total") or {}
            customer_reports[state]["Total"]["Count"] = customer_reports.get(state).get("Total").get("Count") or 0
            customer_reports[state]["Total"]["Count"] = customer_reports.get(state).get("Total").get("Count") + 1

            customer_reports[state]["C2Cs on New Platform"] = customer_reports.get(state).get("C2Cs on New Platform") or {}
            customer_reports[state]["C2Cs on New Platform"]["Count"] = customer_reports.get(state).get("C2Cs on New Platform").get("Count") or 0
            
            
            customer_reports[state][district] = customer_reports.get(state).get(district) or {}

            customer_reports[state][district]["Total"] = customer_reports.get(state).get(district).get("Total") or {}
            customer_reports[state][district]["Total"]["Count"] = customer_reports.get(state).get(district).get("Total").get("Count") or 0
            customer_reports[state][district]["Total"]["Count"] = customer_reports.get(state).get(district).get("Total").get("Count") + 1

            customer_reports[state][district][hub] = customer_reports.get(state).get(district).get(hub) or {}
            customer_reports[state][district][hub]["Count"] = customer_reports.get(state).get(district).get(hub).get("Count") or 0
            customer_reports[state][district][hub]["Count"] = customer_reports.get(state).get(district).get(hub).get("Count") + 1
            
            # customer_reports[state][hub]= customer_reports.get(state).get(hub) or {}
            # customer_reports[state][hub]["Count"] = customer_reports.get(state).get(hub).get("Count") or 0
            # customer_reports[state][hub]["Count"] = customer_reports.get(state).get(hub).get("Count") + 1
            customer_count.append(row["Mobile"])
            count_total_customer += 1
    
    customer_reports["Total"] = customer_reports.get("Total") or {}
    customer_reports["Total"]["Count"] = count_total_customer
    s = set(customer_count)
    print("total farmers count   =   "+ format(len(s)))
    
    with open("customer_report.json" , 'w') as f:
        json.dump(customer_reports, f)

    return customer_reports
