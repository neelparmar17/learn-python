import csv
import json
from datetime import date, timedelta

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
