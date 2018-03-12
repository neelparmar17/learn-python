today=$(date "+%d/%m/%Y")
yesterday=$(date -d "yesterday" "+%d/%m/%Y")
starting=$(date "+01/%m/%Y")
day_befor_yesterday=$(date -d "-2 day" "+%d/%m/%Y")

echo $starting
echo $yesterday

if [ "$starting" == "$yesterday" ]; then
  echo "equal"
elif [ "$starting" == "$today" ]; then
  echo "equal date go to prev month"
else
  echo "not equal"
fi