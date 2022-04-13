from datetime import datetime
import re
from time import time
from urllib.parse import uses_relative
file = open("authlog.txt","r")
f = file.readlines()
x = False
buffer = []

ipList = []
userList = []
timeList = []

date1 = input("Please enter date 1: (MMM  DD) (i.e: Mar  6)")
date2 = input("Please enter date 2: (MMM  DD) (i.e: Mar  8)")

for i in f:
    if date1 in i:
        buffer.append(i)
        timeList.append(i[:16])
        x = True 
    elif date2 in i:
        buffer.append(i)
        timeList.append(i[:16])
        x = False
    elif x:
        buffer.append(i)
        timeList.append(i[:16])

for i in buffer:
    y = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",i)
    z = re.search(r"(?<=\bfor user\s)(\w+)",i)
    #print(z)
    if y:
        ipList.append(y.group(1))
    if z:
        userList.append(z.group(1))

ipDictionary = {}
for i in set(ipList):
    ipDictionary[i] = ipList.count(i)

print(userList)
print(ipList)
print(timeList)
