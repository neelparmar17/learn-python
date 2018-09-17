today=$(date "+%d/%m/%Y")
yesterday=$(date -d "yesterday" "+%d/%m/%Y")
starting=$(date "+01/%m/%Y")
day_before_yesterday=$(date -d "-2 day" "+%d/%m/%Y")


curl -k https://trringo-reporting-prod.pt2sm2efbx.ap-south-1.elasticbeanstalk.com/squealy/orders/download -o orders.xlsx

if [ "$starting" == "$yesterday" ]; then
  curl -d "field=1919191919&password=marketing" -X POST -c myCoookie http://old.trringology.com/users/login
  curl -b myCoookie -X POST -d "dateRange=$day_before_yesterday - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports --header "Content-Type:application/x-www-form-urlencoded" -o orders_report.csv
  curl -b myCoookie -X POST -d "dateRange=$day_before_yesterday - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/implement_report --header "Content-Type:application/x-www-form-urlencoded" -o implement_rented_report.csv
  curl -b myCoookie -X POST -d "dateRange=$day_before_yesterday - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/customer_report --header "Content-Type:application/x-www-form-urlencoded" -o customer_report.csv
elif [ "$today" == "$starting" ]; then 
  prev_month=$(date -d "-1 month" "+01/%m/%Y")
  curl -d "field=1919191919&password=marketing" -X POST -c myCoookie http://old.trringology.com/users/login
  curl -b myCoookie -X POST -d "dateRange=$prev_month - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports --header "Content-Type:application/x-www-form-urlencoded" -o orders_report.csv
  curl -b myCoookie -X POST -d "dateRange=$prev_month - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/implement_report --header "Content-Type:application/x-www-form-urlencoded" -o implement_rented_report.csv
  curl -b myCoookie -X POST -d "dateRange=$prev_month - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/customer_report --header "Content-Type:application/x-www-form-urlencoded" -o customer_report.csv
else
  curl -d "field=1919191919&password=marketing" -X POST -c myCoookie http://old.trringology.com/users/login
  curl -b myCoookie -X POST -d "dateRange=$starting - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports --header "Content-Type:application/x-www-form-urlencoded" -o orders_report.csv
  curl -b myCoookie -X POST -d "dateRange=$starting - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/implement_report --header "Content-Type:application/x-www-form-urlencoded" -o implement_rented_report.csv
  curl -b myCoookie -X POST -d "dateRange=$starting - $yesterday&status=1&action=Export to Excel" http://old.trringology.com/reports/customer_report --header "Content-Type:application/x-www-form-urlencoded" -o customer_report.csv
fi