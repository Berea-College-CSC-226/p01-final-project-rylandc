######################################################################
# Author: Charle Ryland
# Username: rylandc
#
# Purpose:
#
######################################################################
# Acknowledgements:
#
#
#
#
######################################################################
import tkinter as tk

# Section 1: The game stuff.

class NIM:
    def __init__(self):
        """
        The initializer establishes variables used in all the methods.

        """
        bells = 0 # number of bells in the basket currently
        win = ""  # empty string right now, will later be set depending on who takes the last turn
        take = 0  # a constantly changing variable that represents the number of bells being taken
        turn = 1  # manages the turns, odd = player turn, even = computer turn

    def human_turn(self):
        pass

    def comp_turn(self):
        pass

    def run(self): # handles everything related to the actual functioning of the game
        pass
        #print("The game has been run.")

# Section 2: The GUI stuff.

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

    def create_button1(self):
        pass

    def create_textbox1(self):
        pass

    def create_label1(self):
        pass

    def button1_handler(self):
        pass


# Section 3: The main() stuff.

def main():
    """
    Creates an object of the NIM class and calls the method run().

    """
    game = NIM()
    game.run()

main()