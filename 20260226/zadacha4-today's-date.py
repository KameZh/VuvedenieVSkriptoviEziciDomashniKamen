import datetime
today = datetime.date.today()
print("Today's date:", today)
end_of_year = datetime.date(today.year, 12, 31)
daysleft = (end_of_year - today).days
print(f"Time until the end of the year: {daysleft}")