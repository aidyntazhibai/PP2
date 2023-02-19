import datetime

x = datetime.datetime.now()

# Write a Python program to subtract five days from current date.

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)

print(y)

print()
print()
print()

# Write a Python program to print yesterday, today, tomorrow.


print(x - datetime.timedelta(days=1))
print((x - datetime.timedelta(days=1)).strftime("%A"))
print(datetime.datetime.now())
print(x.strftime("%A"))
print(x + datetime.timedelta(days=1))
print((x + datetime.timedelta(days=1)).strftime("%A"))


# Write a Python program to drop microseconds from datetime.

print()
print()
print()


DateWithoutMicro = x.replace(microsecond=0)

print(DateWithoutMicro)


# Write a Python program to calculate two date difference in seconds.


date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')  #strptime used to convert string to date

date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')


differ = (date2 - date1).total_seconds()

#result
print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", differ)

