from datetime import datetime
date1='02/03/2022'
date2='02/05/2024'
# date1=input('Insert first date as dd/mm/yyyy: ')
# date2=input('Insert second date as dd/mm/yyyy: ')
format = "%d/%m/%Y"
date1f = datetime.strptime(date1, format)
date2f = datetime.strptime(date2, format)
diff = date2f - date1f


# Access the days, seconds, and microseconds components
days = diff.days
seconds = diff.seconds
microseconds = diff.microseconds

# Print the results
print(f"Days difference: {days}")
print(f"Seconds difference: {seconds}")
print(f"Microseconds difference: {microseconds}")