file = open("month_folder/august.csv", 'r', )
events = {}
monthCount = file.read()
monthCount = monthCount.split(",")

evtCount = 0
evtDate = 1
for days in monthCount:
    days = days.strip("\n")
    evtCount += 1
    if days != 'august':
        events[days] = ""
    if evtCount > 32 and days != 'august':
        events[str(evtDate)] = days
        evtDate += 1

print(events)
