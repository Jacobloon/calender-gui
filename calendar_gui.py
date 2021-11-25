from tkinter import *
import tkinter as tk
from tkinter.ttk import *

days = 0


# Grabs User Year
def year_submit(event=None):
    global year
    year = int(yearVar.get())
    yearVar.set("")
    print(year)
    yearTk.destroy()


# Grabs User Year
def month_submit(event=None):
    global month
    month = str(monthVar.get()).lower()
    monthVar.set("")
    print(month)
    monthTk.destroy()


# Tkinter Year Menu
yearTk = tk.Tk()
yearVar = tk.StringVar()
startTitle = Label(yearTk, text="Enter the Year:").grid(row=0)
yearEntry = Entry(yearTk, textvariable=yearVar)
yearEntry.focus()
yearEntry.grid(row=1)
buttonYear = Button(yearTk, text="Submit", command=year_submit).grid(row=2)
yearTk.bind('<Return>', year_submit)
yearTk.mainloop()

# Tkinter Month Menu
monthTk = tk.Tk()
monthVar = tk.StringVar()
monthTitle = Label(monthTk, text="Enter the Month:").grid(row=0)
monthEntry = Entry(monthTk, textvariable=monthVar)
monthEntry.focus()
monthEntry.grid(row=1)
buttonMonth = Button(monthTk, text="Submit", command=month_submit).grid(row=2)
monthTk.bind('<Return>', month_submit)
monthTk.mainloop()


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
        start = tk.Tk()
        monthVar = tk.StringVar()
        startTitle = Label(start, text="Enter a valid month:").grid(row=0)
        monthTitle = Entry(start, textvariable=monthVar).grid(row=1)
        buttonTitle = Button(start, text="Submit", command=month_submit).grid(row=2)
        start.bind('<Return>', month_submit)
        start.mainloop()

# Reads current csv
file = open("month_folder/{:s}.csv".format(month), 'r', )
events = {}
monthCount = file.read()
monthCount = monthCount.split(",")

evtCount = 1
evtDate = 1
for days in monthCount:
    days = days.strip(",\n")
    if evtCount <= monthDates["{:s}".format(month)]:
        events[days] = ""
    if evtCount > monthDates["{:s}".format(month)]:
        events[str(evtDate)] = days
        evtDate += 1
    evtCount += 1
days = len(events)

# Creates blank time details dictionary for the given day
#           TODO: CHANGE INTO WRITING INTO A .CSV FILE
hours = {}
for hour in range(24):
    hours[hour+1] = ""


# Viewing events
#           TODO: CHANGE INTO READING THE .CSV FILE
def view_plans():
    plans = False
    for plan in events:
        if events[plan] != "empty":
            plans = True
            print(events[plan])
    if not plans:
        print("No plans scheduled yet\n")


# User selects action for date
#          TODO: Open in new Tkinter window
def date_action():
    actions = Tk()
    actTitle = Label(actions, text="What would you like to do?").grid(row=0, column=1)
    viewButton = Button(actions, text="View Events", command=view_plans).grid(row=1, column=0)
    addButton = Button(actions, text="Add Events").grid(row=1, column=1)
    delButton = Button(actions, text="Delete Events").grid(row=1, column=2)
    '''
    if action_choice == 1:
        view_plans()
   
    if action_choice == 2:
        open()
    '''
    actions.mainloop()


# Tkinter initial window creation
weekDays = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
root = Tk()
myLabel = Label(root, text=month.upper()).grid(row=0, column=3)
for dayNames in weekDays:
    dayLabel = Label(root, text="{:s}".format(dayNames))
    dayLabel.grid(row=1, column=weekDays[dayNames])

# Creates dates as buttons on window
#            TODO: Function to calculate start of month based on year (EX. December 1st on wednesday 2021)
#            TODO: Button returns date value
startColumn = 0
rowCt = 2
columnCt = startColumn
for calDays in range(days):
    dayButton = Button(root, text=calDays+1, command=date_action)
    if columnCt < 7:
        dayButton.grid(row=rowCt, column=columnCt)
        columnCt += 1
    else:
        columnCt = 0
        rowCt += 1
        dayButton.grid(row=rowCt, column=columnCt)
        columnCt += 1
root.mainloop()


'''# Python code to demonstrate the working of
# calendar() and first_weeks_day()

# importing calendar module for calendar operations
import calendar
 
# using calendar to print calendar of year
# prints calendar of 2012
print ("The calendar of year 2012 is : ")
print (calendar.calendar(2012,2,1,6))
 
#using firstweekday() to print starting day number
print ("The starting day number in calendar is : ",end="")
print (calendar.firstweekday())
'''