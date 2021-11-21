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
    if not found:
        month = input("Enter a Valid Month: ").lower()

# Creates blank events dictionary for the given month
events = {}
count = 1
while count <= days:
    events[count] = ""
    count += 1

# User selects date
userChoice = int(input("Enter a date: "))
found = False
while not found:
    for date in events:
        if not found:
            if userChoice == date:
                selectDate = date
                found = True
    if not found:
        userChoice = int(input("Enter a Valid Date: "))

# Creates blank time details dictionary for the given day
#           CHANGE INTO WRITING INTO A .CSV FILE
hours = {}
for hour in range(24):
    hours[hour+1] = ""


# Viewing events
#           CHANGE INTO READING THE .CSV FILE
def view_plans():
    plans = False
    for plan in hours:
        if hours[plan] != "":
            plans = True
            print("{:d}:00 ~ {:s}".format(events, hours[plan]))
    if not plans:
        print("No plans scheduled yet\n")


# User selects action for date
actionChoice = int(input("What would you like to do?: \n"
                         "1) ~VIEW EVENTS~\n"
                         "2) ~ADD EVENTS~\n"
                         "3) ~DELETE EVENTS\n"))

while actionChoice < 1 or actionChoice > 2:
    actionChoice = int(input("Please enter a valid choice: \n"
                             "1) ~VIEW EVENTS~\n"
                             "2) ~ADD EVENTS~\n"
                             "3) ~DELETE EVENTS~\n"))
if actionChoice == 1:
    view_plans()
