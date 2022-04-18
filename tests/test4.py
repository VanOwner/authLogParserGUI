from datetime import datetime

file = open("authlog.txt", "r")
f = file.readlines()
date = []
for i in f:
    dateTemp = i[0:15]
    date.append(datetime.strptime(dateTemp, "%b %d %X"))

print(date[0])
print(dateTemp)