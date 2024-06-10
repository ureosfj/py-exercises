import calendar

m = int(input('give month: '))
y = int(input('give year: '))

cal = calendar.TextCalendar()
print(cal.formatmonth(y, m))