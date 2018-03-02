#!/bin/bash

today=$(date "+%d/%m/%Y")
yesterday=$(date -d "yesterday" "+%d/%m/%Y")
starting=$(date --date="-1 month" "+%d/%m/%Y")

echo $starting
echo $yesterday
curl -d "field=1919191919&password=marketing" -X POST -c myCoookie http://trringology.com/users/login
curl -b myCoookie -X POST -d "dateRange=$starting - 27/02/2018&status=1&action=Export to Excel" http://trringology.com/reports --header "Content-Type:application/x-www-form-urlencoded" -o orders_report.csv
curl -b myCoookie -X POST -d "dateRange=$starting - 27/02/2018&status=1&action=Export to Excel" http://trringology.com/reports/implement_report --header "Content-Type:application/x-www-form-urlencoded" -o implement_rented_report.csv
curl -b myCoookie -X POST -d "dateRange=$starting - 27/02/2018&status=1&action=Export to Excel" http://trringology.com/reports/customer_report --header "Content-Type:application/x-www-form-urlencoded" -o customer_report.csv


echo "done running"