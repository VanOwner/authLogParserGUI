import re
from datetime import datetime, timedelta
from time import strptime
from breezypythongui import EasyFrame
import tkinter

from breezypythongui import END

f = open("authlog.txt", "r")

read_lines = f.readlines()


class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=500, height=300,
                           title="Programming Project 3")
        self.addLabel(font=("Verdana", 20, "bold"), text="CSCI 1523 - Search authlog.txt file",row=0, column=0, columnspan=5, sticky="NSEW")

        self.addLabel(font=("Verdana", 16), text="Start Date (mm/dd): ",row=2, column=0, columnspan=2, sticky="NEW")
        self.startDateTemp = self.addTextField(text="", row=2, column=3, columnspan=1, sticky="NEW")
        

        self.addLabel(font=("Verdana", 16), text="End Date (mm/dd): ",row=2, column=0, columnspan=2, sticky="SEW")
        self.endDateTemp = self.addTextField(text="", row=2, column=3, sticky="SEW")

        self.addButton(text="Search", row=2, column=4, command=self.search())


        self.addLabel(font=("Verdana", 13), text="Login Attempts",row=3, column=0, columnspan=5, sticky="EW")


    def search(self):
        buffer = []
        date = []
        dateList = []

        startDateTemp = self.startDateTemp.getText()
        endDateTemp = self.endDateTemp.getText()

        print(startDateTemp)
        print(endDateTemp)
        #month1 = int(startDateTemp[0:2])
        #day1 = int(startDateTemp[3:])

        #month2 = int(endDateTemp[0:2])
        #day2 = int(endDateTemp[3:])
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
            return print(i)



def main():
    LayoutDemo().mainloop()


if __name__ == "__main__":
    main()
