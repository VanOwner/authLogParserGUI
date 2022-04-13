from breezypythongui import EasyFrame


class layoutDemo(EasyFrame):
    # displays labels in the quadrents

    def __init__(self):
        # Sets up the window
        EasyFrame.__init__(self)

        self.addLabel(text = ("0,0"), row = 0, column = 0)
        self.addLabel(text = ("0,1"), row = 0, column = 1)
        self.addLabel(text = ("1,0"), row = 1, column = 0)
        self.addLabel(text = ("1,1"), row = 1, column = 1)

def main():
    layoutDemo().mainloop() 

if __name__ == "__main__":  
    main()
