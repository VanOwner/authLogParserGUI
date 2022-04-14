import re
from breezypythongui import EasyFrame
import tkinter

file = open("authlog.txt", "r")

read_lines = file.readlines()

class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 500, height = 300, title = "Programming Project 3")
        self.addLabel(font = ("Verdana", 20, "bold"), text = "CSCI 1523 - Search authlog.txt file", row = 0, column = 0, columnspan = 5, sticky = "NSEW")

        self.addLabel(font = ("Verdana", 16), text = "Start Date: ", row = 2, column = 0, columnspan = 2, sticky = "NEW")
        self.startDate = self.addTextField(text = "", row = 2, column = 3, columnspan = 1, sticky = "NEW")
        
        self.addButton(text = "Search", row = 2, column = 4, command = self.search)

        self.addLabel(font = ("Verdana", 16), text = "End Date: ", row = 2, column = 0, columnspan = 2, sticky = "SEW")
        self.endDate = self.addTextField(text = "", row = 2, column = 3, sticky = "SEW")

        self.addLabel(font = ("Verdana", 13), text = "Login Attempts", row = 3, column = 0, columnspan = 5, sticky = "EW")
        self.loginAttempts = self.addTextField(text = "", row = 3, column = 3, state = "readonly", sticky = "SEW")

    def search(self):
        start_date = self.startDate.getText()
        end_date = self.endDate.getText()

        data = ""

        for i in reversed(read_lines):
            if start_date in i:
                data += i
            if end_date in i:
                break

        ip_list = []
        for k in data.split():
            pattern = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", k)
            if pattern:
                ip_list.append(pattern.group(1))

        ip_dict = {}
        for j in set(ip_list):
	        ip_dict[j] = ip_list.count(j)

        for ip, amount in ip_dict.items():
            print(f"{ip}")
        
        self.loginAttempts.setText(data)

def main():
    LayoutDemo().mainloop()
if __name__ == "__main__":
    main()

