import csv
import json
from datetime import date, timedelta
import pyexcel as pe

from generate_html_func import generate_html, generate_daily_report_html
from tractor_harvestor_report import transform_data, transform_orders
from customer_report import transform_data_customer
from c2c_franchisee_report import transform_data_c2c_franchisee
from aggregate_data import aggregate_data, aggregate_data_c2c_franchisee
from implement_rented import transform_data_implement, transform_data_implement_new_pf
# import subprocess 




def generate_daily_report():
    # subprocess.call("./automate.sh")
    yesterday = date.today() - timedelta(1)
    
    orders = transform_data("Order_Report_12Mar18.csv", yesterday)
    implements = transform_data_implement("'Implement_Report_12Mar18'.csv", yesterday)
    customers = transform_data_customer("'Customer_Report_12Mar18'.csv", yesterday)
    c2c_franchinsee = transform_data_c2c_franchisee("Order_Report_12Mar18.csv", "Orders New PF-12Mar.xlsx", yesterday)
    final_orders = transform_orders(orders,   "Orders New PF-12Mar.xlsx")
    final_implements = transform_data_implement_new_pf(implements, "Orders New PF-12Mar.xlsx", yesterday)
    
    aggregate_daily_report = aggregate_data(final_orders, final_implements, customers)
    aggregate_c2c_franchisee = aggregate_data_c2c_franchisee(c2c_franchinsee, final_orders)

    email_html = generate_html(aggregate_daily_report, yesterday)
    report_html = generate_daily_report_html(aggregate_c2c_franchisee, email_html, yesterday, final_orders)
    with open("report.html", 'w') as html:
        html.write(email_html)
    
    with open("full_report.html", 'w') as full_html:
        full_html.write(report_html)
    
    return report_html


generate_daily_report()