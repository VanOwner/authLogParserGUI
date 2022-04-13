"""
File: canvasdemo1.py
"""

from breezypythongui import EasyFrame, EasyCanvas
import random

class CanvasDemo(EasyFrame):
    """Draws filled ovals and messages on a canvas."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Canvas Demo 1")

        # Canvas
        self.canvas = self.addCanvas(row = 0, column = 0,
                                     columnspan = 3,
                                     width = 400, height = 200)
        self.canvas["background"] = "gray"
        
        # Command buttons
        self.ovalButton = self.addButton(text = "Draw oval",
                                         row = 1, column = 0,
                                         command = self.drawOval)
        self.textButton = self.addButton(text = "Draw text",
                                         row = 1, column = 1,
                                         command = self.drawText)
        self.clearButton = self.addButton(text = "Clear all",
                                          row = 1, column = 2,
                                          command = self.clearAll)
        
        # Holds the IDs of the shapes after they're drawn
        self.items = list()

    # Event handler methods for the command buttons

    def drawOval(self):
        """Draws a filled oval at a random position."""
        x = random.randint(20, 350)
        y = random.randint(20, 120)
        self.items.append(self.canvas.drawOval(x, y, x + 25, y + 25,
                                               fill = "blue"))

    def drawText(self):
        """Draws 'Hello world!' at a random position."""
        x = random.randint(20, 350)
        y = random.randint(20, 120)
        self.items.append(self.canvas.drawText("Hello world!", x, y,
                                               fill = "red"))

    def clearAll(self):
        """Deletes all the shapes from the canvas."""
        for item in self.items:
            self.canvas.deleteItem(item)
        self.items = list()



# Instantiate and pop up the window."""
CanvasDemo().mainloop()
