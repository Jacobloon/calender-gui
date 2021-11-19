# Starting Variables
year = float(input("Enter the Year : "))
month = input("Enter the Month : ").lower()
days = 0

# Calculate February on Leap Years
if year % 4 == 0:
    if (year % 100 == 0) and (year % 400 == 0):
        febNum = 29
    elif year % 100 == 0:
        febNum = 28
    else:
        febNum = 29
else:
    febNum = 28

# Define {Month: Dates} in a Dictionary
monthDates = {"january": 31, "february": febNum, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
              "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}

# Define number of days in chosen month
found = False
while not found:
    for months in monthDates:
        if month == months:
            found = True
            days = monthDates[months]
            print(days)
    if not found:
        month = input("Enter a Valid Month: ").lower()

# Creates blank events dictionary for the given month
events = {}
count = 1
while count <= days:
    events[count] = ""
    count += 1
