# program to display the calendar of the given month and the year
import calendar

# given the year and the month
# year = 2021
# month = 12
# incase you want to take the month and the year from the user
year = int(input("Enter the year :"))
month = int(input("Enter the month of the year :"))

print(calendar.month(year, month))
