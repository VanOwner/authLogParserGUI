from breezypythongui import EasyFrame

class layoutDemo(EasyFrame):
    # displays labels in the quadrents

    def __init__(self):
        # Sets up the window
        EasyFrame.__init__(self, width=500, height=300,
                           title="Programming Project 3")

        self.addLabel(font=("Verdana", 20, "bold"), text="CSCI 1523 - Search authlog.txt file",row=0, column=0, columnspan=5, sticky="NSEW")

        self.addLabel(font=("Verdana", 16), text="Start Date (mm/dd): ",row=2, column=0, columnspan=2, sticky="NEW")
        self.startDateTemp = self.addTextField(text="", row=2, column=3, columnspan=1, sticky="NEW")
        
        self.addLabel(font=("Verdana", 16), text="End Date (mm/dd): ",row=2, column=0, columnspan=2, sticky="SEW")
        self.endDateTemp = self.addTextField(text="", row=2, column=3, sticky="SEW")

        self.addButton(text="Search", row=2, column=4, command=self.search())

        self.addLabel(font=("Verdana", 13), text="Login Attempts",row=3, column=0, columnspan=5, sticky="EW")
        self.outputField = self.addTextField(text=" ",row=4,column=1,state="readonly")

    def search(self):
        startDateTemp = self.startDateTemp.getText()
        endDateTemp = self.endDateTemp.getText()

        month1 = startDateTemp[0:2]
        day1 = startDateTemp[3:]

        month2 = endDateTemp[0:2]
        day2 = endDateTemp[3:]

        print(startDateTemp)
        self.outputField.setText(month1)
def main():
    layoutDemo().mainloop() 

if __name__ == "__main__":  
    main()
