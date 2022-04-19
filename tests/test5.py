from breezypythongui import EasyFrame
from breezypythongui import END


class layoutDemo(EasyFrame):
    # displays labels in the quadrents

    def __init__(self):
        # Sets up the window
        # Sets up the window
        EasyFrame.__init__(self, width=600, height=400,title="Programming Project 3")
        self.addLabel(font = ("Verdana", 20, "bold"), text = "CSCI 1523 - Search authlog.txt file", row = 0, column = 0, columnspan = 5, sticky = "NSEW")
        self.addButton(text = "Search", row = 2, column = 4, command = self.search)

        self.listBox = self.addListbox(row = 5, column = 3)
        #self.listItemSelected(0)
    def search(self):
        fruit=["apple","orange","tomato","banana"]

        for i in fruit:
            self.listBox.insert(END,i)

def main():
    layoutDemo().mainloop() 

if __name__ == "__main__":  
    main()
