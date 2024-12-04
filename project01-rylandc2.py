######################################################################
# Author: Charle Ryland
# Username: rylandc
#
# Purpose:
#
######################################################################
# Acknowledgements:
# I consulted the TA, Nicholas, to figure out how to get the classes to interact the way I need them to.
#
#
#
######################################################################
import tkinter as tk
from game_class import NIM


# Section 1: The GUI stuff.

class Visual:
    """
    Responsible for everything GUI.

    TODO: GUI get set up correctly.
    """
    def __init__(self):
        """
        The initializer instantiates a window for the widgets.

        """
        self.root = tk.Tk()
        self.root.minsize(width=300, height=300)
        self.root.maxsize(width=300, height=300)
        self.root.title("Game of NIM")

        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1 = None

        self.game = NIM()

        self.labeltext = str("There are " + str(self.game.bells) + " bells in the basket.")

    def wn_setup(self):
        self.create_button1()
        self.create_textbox1()
        self.create_label1()

    def create_button1(self):
        self.myButton1 = tk.Button(self. root, text="Take bells", command=self.button1_handler)
        self.myButton1.grid(row=0, column=0) # top of the window

    def create_textbox1(self):
        self.myTextBox1.grid(row=0, column=1) # middle of the window

    def get_entry(self):
        """
        Retrieves the textbox entry, to be called in NIM.run().
        Only works if it's a number between 1 and 4 inclusive.

        :return: what the user entered in the textbox
        """
        text = self.myTextBox1.get()
        if 1 <= text <= 4: # if the number entered is between 1 and 4 inclusive
            return text

    def create_label1(self):
        self.myTextLabel1 = tk.Label(self.root, textvariable= self.labeltext)
        self.myTextLabel1.grid(row=0, column=2) # bottom of the window

    def button1_handler(self):
        """
        Event handler for button1 above.
        Takes the input number of bells (if within acceptable range) and subtracts it from total.

        """
        pass


# Section 2: The main() stuff.

def main():
    """
    Creates an object of the NIM class and calls the method run().

    """
    #game = NIM()  # initialize the game object.
    wn = Visual() # the screen used for the game
    wn.wn_setup()
    #game.run(wn)  # run the game, passing in the Visual so it can be used.

main()