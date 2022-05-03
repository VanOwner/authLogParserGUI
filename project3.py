'''
Program: PP03Csci1523Spr2022 Csci 1523 Programming Project 3
Author: John Bennett
Date: 04/25/2022
Purpose: 

1. Using the authlog.txt file provided here please prepare a GUI front end that will allow a user to enter a beginning date into a input box and an ending date into an input box.
2. Using the two dates entered write a Python script that opens the file and retrieves all the logon attempts within the date range provided.
3. Extract the following from each line: date, time, IP address and user name. These are to be placed into a scroll box so that the user can scroll forward and back to review the data.

'''


# imports
import re
from datetime import datetime, timedelta
from time import strptime
from breezypythongui import EasyFrame
from breezypythongui import EasyListbox
import tkinter

from breezypythongui import END

file = open("authlog.txt", "r")

f = file.readlines()

# GUI calls
class LayoutDemo(EasyFrame):
    def __init__(self):
        # Sets up the window
        EasyFrame.__init__(self, width=600, height=400,title="Programming Project 3")

        # label setup for title
        self.addLabel(font = ("Verdana", 20, "bold"), text = "Search Authlog.txt logins by date", row = 0, column = 0, columnspan = 5, sticky = "NSEW")

        # start date label
        self.addLabel(font = ("Verdana", 16), text = "Start Date (mm/dd): ", row = 2, column = 0, columnspan = 2, sticky = "NEW")
        self.startDate = self.addTextField(text = "", row = 2, column = 3, columnspan = 1, sticky = "NEW")

        # Search button
        self.addButton(text = "Search", row = 2, column = 4, command = self.search)

        # end date label    
        self.addLabel(font = ("Verdana", 16), text = "End Date (mm/dd): ", row = 2, column = 0, columnspan = 2, sticky = "SEW")
        self.endDate = self.addTextField(text = "", row = 2, column = 3, sticky = "SEW")

        # login attempt label
        self.addLabel(font = ("Verdana", 13), text = "Login Attempts", row = 3, column = 0, columnspan = 5, sticky = "EW")

        # List box setup
        self.listBox = self.addListbox(row = 4, column = 1, columnspan = 3)
        

    # Search function
    def search(self):
        buffer = []
        date = []
        dateList = []
        
        # get text from text boxes add to variable
        startDateTemp = self.startDate.getText()
        endDateTemp = self.endDate.getText()

        # create new variables of only the times
        month1 = int(startDateTemp[0:2])
        day1 = int(startDateTemp[3:])

        month2 = int(endDateTemp[0:2])
        day2 = int(endDateTemp[3:])
        
        
        # converts inputted dates to datetime and then back to a formatted string
        startDate = datetime(1900,month1, day1)

        endDate = datetime(1900,month2, day2)
        
        
        print(startDate)
        print(endDate)
        
        x = True

        # start of for loop
        for i in f:

            # create date temp of I to 15th character
            dateTemp = i[0:15]  

            # create datetime object of datetemp
            date = (datetime.strptime(dateTemp, "%b %d %X"))

            # conditional to check if dates are in between
            if endDate+timedelta(days=1)>date>startDate:

                # Regex parse out IP and User
                y = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",i)
                z = re.search(r"(?<=\buser\s)(\w+)",i)

                # if regex finds something append everything together into dateList
                if y and z:
                    dateList.append("Login on "+date.strftime("%m/%d %H:%M:%S")+" from user "+z.group(1)+" IP: "+y.group(1))
                elif z:
                    dateList.append("Login on "+date.strftime("%m/%d %H:%M:%S")+" from user "+z.group(1)+" with no IP")
        
        # sort datelist and print into listbox
        dateList.sort()
        for i in dateList:
            self.listBox.insert(END,i)

# main function
def main():
    LayoutDemo().mainloop()


if __name__ == "__main__":
    main()
