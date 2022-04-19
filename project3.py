import re
from datetime import datetime, timedelta
from time import strptime
file = open("authlog.txt", "r")
f = file.readlines()
x = False
buffer = []
date = []
dateList = []
ipList = []
userList = []
timeList = []


# input dates
startDateTemp = input('Enter a starting date (mm/dd): ')
endDateTemp = input('Enter a ending date (mm/dd): ')

month1 = int(startDateTemp[0:2])
day1 = int(startDateTemp[3:])

month2 = int(endDateTemp[0:2])
day2 = int(endDateTemp[3:])
# converts inputted dates to datetime and then back to a formatted string
startDate = datetime(1900,month1, day1)

endDate = datetime(1900,month2, day2)


print(startDate)
print(endDate)


for i in f:
    dateTemp = i[0:15]
    date = (datetime.strptime(dateTemp, "%b %d %X"))
    y = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",i)
    z = re.search(r"(?<=\bfor user\s)(\w+)",i)
    
    if endDate+timedelta(days=1)>date>startDate:
        dateList.append("Login on "+date.strftime("%m/%d %H:%M:%S"))
        y = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",i)
        z = re.search(r"(?<=\bfor user\s)(\w+)",i)
        if y:
            dateList.append("ip: "+y.group(1))
        if z:
            dateList.append("from user "+z.group(1))	

        
        
        


for i in dateList:
    print(i)
#print(timeList)

