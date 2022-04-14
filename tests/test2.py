date1 = input("Please enter starting date: (mm/dd)")
date2 = input("Please enter end date: (mm/dd)")

month1 = int(date1[0:2])
day1 = int(date1[3:])
month2 = int(date2[0:2])
day2 = int(date2[3:])


def startDateMatch(month1, day1):
    Start=""
    if month1 == 1:
        Start = "Jan"
    elif month1 == 2:
        Start = "Feb"
    elif month1 == 3:
        Start = "Mar"
    elif month1 == 4:
        Start = "Apr"   
    elif month1 == 5:
        Start = "May"
    elif month1 == 6:
        Start = "Jun"   
    elif month1 == 7:
        Start = "Jul"
    elif month1 == 8:
        Start = "Aug"
    elif month1 == 9:
        Start = "Seb"
    elif month1 == 10:
        Start = "Oct"
    elif month1 == 11:
        Start = "Nov"
    elif month1 == 12:
        Start = "Dec"
    else:
        pass
    return Start+ " "+str(day1)

def endDateMatch(month2, day2):
    Start=""
    if month2 == 1:
        End = "Jan"
    elif month2 == 2:
        End = "Feb"
    elif month2 == 3:
        End = "Mar"
    elif month2 == 4:
        End = "Apr"   
    elif month2 == 5:
        End = "May"
    elif month2 == 6:
        End = "Jun"   
    elif month2 == 7:
        End = "Jul"
    elif month2 == 8:
        End = "Aug"
    elif month2 == 9:
        End = "Seb"
    elif month2 == 10:
        End = "Oct"
    elif month2 == 11:
        End = "Nov"
    elif month2 == 12:
        End = "Dec"
    else:
        pass
    return End+ " "+str(day2)

print(startDateMatch(month1,day1))
print(endDateMatch(month2,day2))

