'''
Program: PP02Csci1523Spr2022 Csci 1523 Programming Project 2
Author: John Bennett
Date: 03/15/2022
Purpose: Parses through an Ubuntu server AuthLog file and:

1. Opens the file and reads the file line-by-line
2. Prints out the time and date of the first attempted login.
3. Prints out the time and date of last attempted login.
4. Count the number of login attempts
5. Counts the number of failed logins, which means those for which the attempt failed due to password authentication failure.
6. Determines by IP address found in the file the number of attempted logins.
So you would count for example how many times a login was attempted
from a specific IP such as 197.223.23.23.
'''
# Import Regex and time
import re
import time 

# Variables
successCount = 0
failedCount = 0
attemptCount = 0
lineCount = 0
lineNum = len(open("authlog.txt").readlines())
elseCount = 0
printing = False

print("This will take a while")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")

# Opens authlog file
file = open("authlog.txt","r")
f = file.readlines()

# Loop through text
for i in f:
    # Line counter
    lineCount+=1

    # Counting successful attempts
    if 'opened' in i:
        successCount+=1
        # Counts attempts
        attempts=+1
    
    # Counting failed attempts
    elif 'Failed password' in i:
        failedCount+=1
        # Counts attempts
        attempts=+1
    else:
        elseCount=+1


# Parse for ips with regex
ipList = []
for i in f:
    # 
    x = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",i)
    if x:
        ipList.append(x.group(1))

# Converts ip list to dictionary
ipDictionary = {}
for i in set(ipList):
    ipDictionary[i] = ipList.count(i)

# Prints and formats so it's readable
for ip, count in ipDictionary.items(): 
        print("\n{} tried to login: {} times".format(ip, count))

print("\n----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

# Check and prints time of first attempt
for i in f:
    if 'opened' in i:
        print("\nThe date of the first attempted login was: "+i[:16])
        break

# Check and prints time of last attempt
for i in reversed(f):
    if ('Failed password') in i:
        print("\nThe date of the last attempted login was: "+i[:16])
        break

date1 = input("Enter date 1: ")
date2 = input("Enter date 2: ")

for i in f:
    if i.startswith(date1):
        printing = True
        continue # go to next line
    elif i.startswith(date2):
        printing = False
        break # quit file reading

if printing:
    print(i, file=f)

# Prints failed login attempts
print("\nThere were",failedCount,"failed login attempts.")
# Prints successful login attempts
print("\nThere were",successCount,"successful login attempts.")
# Prints line numbers
print("\nNumber of lines in text file: ",lineNum)
        

