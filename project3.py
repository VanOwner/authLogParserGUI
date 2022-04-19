import re
from datetime import datetime, timedelta
from time import strptime
from breezypythongui import EasyFrame
from breezypythongui import EasyListbox
import tkinter

from breezypythongui import END

file = open("authlog.txt", "r")

f = file.readlines()


class LayoutDemo(EasyFrame):
    def __init__(self):
        # Sets up the window
        EasyFrame.__init__(self, width=600, height=400,title="Programming Project 3")
        self.addLabel(font = ("Verdana", 20, "bold"), text = "Search Authlog.txt logins by date", row = 0, column = 0, columnspan = 5, sticky = "NSEW")

        self.addLabel(font = ("Verdana", 16), text = "Start Date (mm/dd): ", row = 2, column = 0, columnspan = 2, sticky = "NEW")
        self.startDate = self.addTextField(text = "", row = 2, column = 3, columnspan = 1, sticky = "NEW")

        self.addButton(text = "Search", row = 2, column = 4, command = self.search)

        self.addLabel(font = ("Verdana", 16), text = "End Date (mm/dd): ", row = 2, column = 0, columnspan = 2, sticky = "SEW")
        self.endDate = self.addTextField(text = "", row = 2, column = 3, sticky = "SEW")

        self.addLabel(font = ("Verdana", 13), text = "Login Attempts", row = 3, column = 0, columnspan = 5, sticky = "EW")

        self.listBox = self.addListbox(row = 4, column = 1, columnspan = 3)
        


    def search(self):
        buffer = []
        date = []
        dateList = []
        

        startDateTemp = self.startDate.getText()
        endDateTemp = self.endDate.getText()

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
            self.listBox.insert(END,i)

def main():
    LayoutDemo().mainloop()


if __name__ == "__main__":
    main()
