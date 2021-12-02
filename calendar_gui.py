from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import math

days = 0
febNum = 28
year = 2021

# Calculate February on Leap Years
def leap_year():
    global febNum
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            febNum = 29
        elif year % 100 == 0:
            febNum = 28
        else:
            febNum = 29
    else:
        febNum = 28


# Grabs User Year
def year_submit(event=None):
    global year
    year = int(yearVar.get())
    yearVar.set("")
#    leap_year()
    yearTk.destroy()


# Grabs User Year
def month_submit(event=None):
    global month
    month = str(monthVar.get()).lower()
    monthVar.set("")
    monthTk.destroy()


# Grabs User Date
def date_submit(event=None):
    global date
    date = int(dateEntry.get())
    if date < 1 or date > days:
        dateTk.destroy()
        date_entry()
        return("ouch")
    else:
        date_choices()


# Tkinter Year Menu
'''
yearTk = tk.Tk()
yearVar = tk.StringVar()
startTitle = Label(yearTk, text="Enter the Year:").grid(row=0)
yearEntry = Entry(yearTk, textvariable=yearVar)
yearEntry.focus()
yearEntry.grid(row=1)
buttonYear = Button(yearTk, text="Submit", command=year_submit).grid(row=2)
yearTk.bind('<Return>', year_submit)
yearTk.mainloop()
'''

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

# Define {Month: Dates} in a Dictionary
monthDates = {"january": 31, "february": febNum, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
              "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
monthNums = {"january": 11, "february": 12, "march": 1, "april": 2, "may": 3, "june": 4, "july": 5, "august": 6,
             "september": 7, "october": 8, "november": 9, "december": 10}
monthStarts = {"january": 5, "february": 1, "march": 1, "april": 4, "may": 6, "june": 2, "july": 4, "august": 0,
             "september": 3, "october": 5, "november": 1, "december": 3}

# Define number of days in chosen month
found = False
while not found:
    for months in monthDates:
        if month == months:
            found = True
            days = monthDates[months]
    if not found:
        monthTk = tk.Tk()
        monthVar = tk.StringVar()
        startTitle = Label(monthTk, text="Enter a valid month:").grid(row=0)
        monthTitle = Entry(monthTk, textvariable=monthVar).grid(row=1)
        buttonTitle = Button(monthTk, text="Submit", command=month_submit).grid(row=2)
        monthTk.bind('<Return>', month_submit)
        monthTk.mainloop()

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


# Writes data to current csv
def rewrite():
    f = open("month_folder/{:s}.csv".format(month), 'w', )
    f.truncate(0)
    newFile = []
    fnEvts = []
    for days in events:
        fnEvts.append(events[days])
        newFile.append(days)
    newFile.append("\n")
    for plans in fnEvts:
        newFile.append(plans)
    newfile = "".join(newFile)
    f.write(newFile)
    f.close()
    

# Viewing events (Use 'date' variable for selected date)
#           TODO: fix output format Ex. On the 3rd, this is happening
def view_plans():
    global viewTk
    viewTk = Tk()
    if events[str(date)] != "empty":
        view_title = Label(viewTk, text=events[str(date)]).grid(row=0, column=0)
        print(events[str(date)])
    else:
        view_title = Label(viewTk, text="No plans scheduled, yet!").grid(row=0, column=0)
        print("No plans scheduled yet\n")
    con_bt = Button(viewTk, text="Continue", command=menu_close).grid(row=1, column=0)
    viewTk.bind('<Return>', menu_close)
    viewTk.mainloop()

def menu_close():
    viewTk.destroy()
    dateTk.destroy()
    actionsTk.destroy()
    
    
# Create new events for dates
def add_submit(event=None):
    newEvent = str(addEntry.get())
    events[str(date)] = newEvent
    rewrite()
    addTk.destroy()
    dateTk.destroy()
    actionsTk.destroy()

def add_plans():
    global addEntry
    global addTk
    addTk = Tk()
    addVar = tk.StringVar()
    addLabel = Label(addTk, text="Add your new event below:").grid(row=0, column=0)
    addEntry = Entry(addTk, textvariable=addVar)
    addEntry.grid(row=1, column=0)
    addEntry.focus()
    addButton = Button(addTk, text="Continue", command=add_submit).grid(row=2, column=0)
    addTk.bind('<Return>', add_submit)
    addTk.mainloop()    


# User selects action for date 
def date_choices():
    global actionsTk
    actionsTk = Tk()
    act_title = Label(actionsTk, text="What would you like to do?").grid(row=0, column=1)
    view_button = Button(actionsTk, text="View Events", command=view_plans).grid(row=1, column=0)
    add_button = Button(actionsTk, text="Add Events", command=add_plans).grid(row=1, column=1)
    del_button = Button(actionsTk, text="Delete Events").grid(row=1, column=2)
    actionsTk.mainloop()


# Grabs user's date
def date_entry():
    global dateEntry
    global dateTk
    dateTk = tk.Tk()
    dateVar = tk.StringVar()
    dateLabel = Label(dateTk, text="Enter the Date:").grid(row=0)
    dateEntry = Entry(dateTk, textvariable=dateVar)
    dateEntry.focus()
    dateEntry.grid(row=1)
    dateButton = Button(dateTk, text="Submit", command=date_submit).grid(row=2)
    dateTk.bind('<Return>', date_submit)
    dateTk.mainloop()


# Tkinter initial window creation
weekDays = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
root = Tk()
myLabel = Label(root, text=month.upper()).grid(row=0, column=3)
for dayNames in weekDays:
    dayLabel = Label(root, text="{:s}".format(dayNames))
    dayLabel.grid(row=1, column=weekDays[dayNames])

# Creates dates as buttons on window
#            TODO: Function to calculate start of month based on year (EX. December 1st on wednesday 2021)
startColumn = monthStarts[month]
rowCt = 2
columnCt = startColumn
dayButton = {}
for calDays in range(days):
    dayButton[calDays] = Button(root, text=calDays+1)
    if columnCt < 7:
        dayButton[calDays].grid(row=rowCt, column=columnCt)
        columnCt += 1
    else:
        columnCt = 0
        rowCt += 1
        dayButton[calDays].grid(row=rowCt, column=columnCt)
        columnCt += 1
actionButton = Button(root, text="Actions", command=date_entry).grid(row=rowCt+1, column=3)
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
