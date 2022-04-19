from calendar import month
from datetime import datetime


startDateTemp = input('Enter a starting date (mm/dd): ')
endDateTemp = input('Enter a ending date (mm/dd): ')

month1 = int(startDateTemp[0:2])
day1 = int(startDateTemp[3:])

month2 = int(endDateTemp[0:2])
day2 = int(endDateTemp[3:])

print(month1)
print(day1)
print(month2)
print(day2)
#print(startDate)
#print(endDate)