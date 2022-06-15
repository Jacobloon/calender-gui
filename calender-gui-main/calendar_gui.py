from tkinter import *
import tkinter as tk
from tkinter.ttk import *

days = 0
febNum = 28
year = 2021
leapYear = False


# Calculate February on Leap Years
def leap_year():
    global febNum
    global leapYear
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            febNum = 29
            leapYear = True
        elif year % 100 == 0:
            febNum = 28
        else:
            febNum = 29
            leapYear = True
    else:
        febNum = 28


# Grabs User Month and Year
def day_submit(event=None):
    global month
    month = str(monthVar.get()).lower()
    monthVar.set("")
    global year
    year = int(yearVar.get())
    yearVar.set("")
    leap_year()
    subTk.destroy()


# Grabs User Date
def date_submit(event=None):
    global date
    date = int(dateEntry.get())
    if date < 1 or date > days:
        dateTk.destroy()
        date_entry()
        return "ouch"
    else:
        date_choices()

# Tkinter Submit Menu
subTk = tk.Tk()
subTk.title("Month")
monthVar = tk.StringVar()
monthTitle = Label(subTk, text="Enter the Month:").grid(row=0)
monthEntry = Entry(subTk, textvariable=monthVar)
monthEntry.focus()
monthEntry.grid(row=1)
buttonMonth = Button(subTk, text="Submit", command=day_submit).grid(row=4)

yearVar = tk.StringVar()
startTitle = Label(subTk, text="Enter the Year:").grid(row=2)
yearEntry = Entry(subTk, textvariable=yearVar)
yearEntry.grid(row=3)

subTk.bind('<Return>', day_submit)
subTk.mainloop()


# Define {Month: Dates} in a Dictionary
monthDates = {"january": 31, "february": febNum, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
              "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
monthNums = {"january": 0, "february": 1, "march": 2, "april": 3, "may": 4, "june": 5, "july": 6, "august": 7,
             "september": 8, "october": 9, "november": 10, "december": 11}
monthList = list(monthNums)
monthStarts = {"january": 5, "february": 1, "march": 1, "april": 4, "may": 6, "june": 2, "july": 4, "august": 0,
               "september": 3, "october": 5, "november": 1, "december": 3}

monthKeyVal = {"january": 1, "february": 4, "march": 4, "april": 0, "may": 2, "june": 5, "july": 0, "august": 3,
               "september": 6, "october": 1, "november": 4, "december": 6}


def month_start_date(monthKeyVal):
    endTwo = year % 100  # Grabs the last 2 digits
    endTwo = (endTwo // 4) + 1
    endTwo += monthKeyVal[month]  # Adds month's key val
    if leapYear and (month == "january" or month == "february"):  # Subtracts 1 for leap years
        endTwo -= 1
        print(endTwo)  # TEST
    endTwo += 6 # TODO Currently hardcoded with 2000's val, 1900=0, 1700=4, 1800=2
    endTwo += (year % 100)
    endTwo = (endTwo % 7) - 1
    if endTwo == -1:
        endTwo = 6
    return endTwo




# Define number of days in chosen month
def num_days():
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
            buttonTitle = Button(monthTk, text="Submit", command=day_submit).grid(row=2)
            monthTk.bind('<Return>', day_submit)
            monthTk.mainloop()

# Reads current csv
def month_select():
    global events
    global mthCt
    global days
    file = open("month_folder/{:s}.csv".format(month), 'r', )
    events = {}
    monthCount = file.read()
    monthCount = monthCount.split("\n")
    mthCt = []
    for chunk in monthCount:
        tempList = chunk.split(",")
        mthCt.extend(tempList)

    # Fixes CSV formatting Issues
    print(mthCt)
    mthCt.remove("")
    mthCt.remove("")

    evtCount = 1
    evtDate = 1
    print(mthCt)
    for days in mthCt:
        days = days.strip(",")
        days = days.strip("\n")
        if evtCount <= monthDates["{:s}".format(month)]:
            events[days] = ""
        if evtCount > monthDates["{:s}".format(month)]:
            events[str(evtDate)] = days
            evtDate += 1
        evtCount += 1
    days = len(events)
month_select()


# Writes data to current csv
def rewrite():
    f = open("month_folder/{:s}.csv".format(month), 'w', )
    f.truncate(0)
    newFile = []
    newerFile = [""]
    fnEvts = []
    print(events)
    for days in events:
        fnEvts.append(events[days])
        newFile.append(days)
    newFile.append("\n")
    newerFile[0] = ",".join(newFile)
    for plans in fnEvts:
        newerFile.append(plans)
    newerFile = ",".join(newerFile)
    f.write(newerFile)
    f.close()
    

# Viewing events (Use 'date' variable for selected date)
#           TODO: fix output format Ex. On the 3rd, this is happening
def view_plans():
    global viewTk
    viewTk = Tk()
    viewTk.title("View Plans")
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
    if newEvent == "":
        return print("error")
    events[str(date)] = newEvent
    rewrite()
    addTk.destroy()
    dateTk.destroy()
    actionsTk.destroy()


def add_plans():
    global addEntry
    global addTk
    addTk = Tk()
    addTk.title("Add Plans")
    addVar = tk.StringVar()
    addLabel = Label(addTk, text="Add your new event below:").grid(row=0, column=0)
    addEntry = Entry(addTk, textvariable=addVar)
    addEntry.grid(row=1, column=0)
    addEntry.focus()
    addButton = Button(addTk, text="Continue", command=add_submit).grid(row=2, column=0)
    addTk.bind('<Return>', add_submit)
    addTk.mainloop()    


# Delete plans
def del_submit(event=None):
    newEvent = "empty"
    events[str(date)] = newEvent
    rewrite()
    delTk.destroy()
    dateTk.destroy()
    actionsTk.destroy()


def del_plans():
    global delTk
    delTk = Tk()
    delTk.title("Delete Plans")
    delVar = tk.StringVar()
    delLabel = Label(delTk, text="Events have been cleared").grid(row=0, column=0)
    delButton = Button(delTk, text="Continue", command=del_submit).grid(row=2, column=0)
    delTk.bind('<Return>', del_submit)
    delTk.mainloop()


# User selects action for date 
def date_choices():
    global actionsTk
    actionsTk = Tk()
    actionsTk.title("Actions")
    act_title = Label(actionsTk, text="What would you like to do?").grid(row=0, column=1)
    view_button = Button(actionsTk, text="View Events", command=view_plans).grid(row=1, column=0)
    add_button = Button(actionsTk, text="Add Events", command=add_plans).grid(row=1, column=1)
    del_button = Button(actionsTk, text="Delete Events", command=del_plans).grid(row=1, column=2)
    actionsTk.mainloop()


# Grabs user's date
def date_entry():
    global dateEntry
    global dateTk
    dateTk = tk.Tk()
    dateTk.title("Date")
    dateVar = tk.StringVar()
    dateLabel = Label(dateTk, text="Enter the Date:").grid(row=0)
    dateEntry = Entry(dateTk, textvariable=dateVar)
    dateEntry.focus()
    dateEntry.grid(row=1)
    dateButton = Button(dateTk, text="Submit", command=date_submit).grid(row=2)
    dateTk.bind('<Return>', date_submit)
    dateTk.mainloop()

# Moves month left or right
def cal_left():
    global month
    index = monthNums[month] - 1
    if index < 0:
        index = 11
    month = monthList[index]
    root.destroy()
    month_select()
    cal_window()

def cal_right():
    global month
    index = monthNums[month] + 1
    if index > 11:
        index = 0
    month = monthList[index]
    root.destroy()
    month_select()
    cal_window()

# Tkinter initial window creation [REQUIRES: month, days]
weekDays = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
def cal_window():
    global root
    root = Tk()
    root.title(month.upper())
    myLabel = Label(root, text=month.upper(), font='bold').grid(row=0, column=3)
    for dayNames in weekDays:
        dayLabel = Label(root, text="{:s}".format(dayNames))
        dayLabel.grid(row=1, column=weekDays[dayNames])
    startColumn = month_start_date(monthKeyVal) # Month starting date
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
    leftBt = Button(root, text="<", command=cal_left).grid(row=rowCt+1, column=2)
    actionButton = Button(root, text="Actions", command=date_entry).grid(row=rowCt+1, column=3)
    rightBt = Button(root, text=">", command=cal_right).grid(row=rowCt+1, column=4)
    root.mainloop()
cal_window()
