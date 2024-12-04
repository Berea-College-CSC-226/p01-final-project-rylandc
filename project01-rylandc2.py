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

    TODO: Receives information from NIM (or will, once I figure out how).
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
        self.myTextBox1 = None
        self.myTextLabel1 = None

        self.game = NIM()

    def wn_setup(self):
        self.create_button1()
        self.create_textbox1()
        self.create_label1() # pass in bells from NIM.

    def create_button1(self):
        self.myButton1 = tk.Button(self. root, text="Take bells", command=self.button1_handler)
        self.myButton1.grid(row=0, column=0)

    def create_textbox1(self):
        pass

    def get_entry(self):
        """
        Retrieves the textbox entry, to be called in NIM.run().
        Only works if it's a number between 1 and 4 inclusive.

        :return: what the user entered in the textbox
        """
        text = self.myTextBox1.get()
        if 1 <= text <= 4: # if the number entered is between 1 and 4 inclusive
            return text

    def create_label1(self, bells):
        labeltext = str("There are " + str(bells) + " bells in the basket.")
        pass

    def button1_handler(self):
        pass


# Section 2: The main() stuff.

def main():
    """
    Creates an object of the NIM class and calls the method run().

    """
    #game = NIM()  # initialize the game object.
    wn = Visual() # the screen used for the game
    #game.run(wn)  # run the game, passing in the Visual so it can be used.

main()