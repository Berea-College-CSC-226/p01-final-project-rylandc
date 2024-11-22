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
import random

# Section 1: The game stuff.

class NIM:
    def __init__(self):
        """
        The initializer establishes variables used in all the methods.

        """
        self.bells = 0 # number of bells in the basket currently
        self.win = "Game not played."  # wrong string right now, will later be set to winner message

    def human_turn(self, bells):
        pass

    def comp_turn(self, bells):
        pass

    def setup(self):
        print("Welcome to the Game of NIM!")
        x = False # the only purpose of this variable is to manage the setup while loops.
        y = False # this is to determine something later
        while not x: # true = player answered, exit the loop, false = need to ask again
            choice = input("Do you need instructions? Y/N: ")
            if choice == "Y":
                print("In this game, there is a basket of 16 or more bells.\n"
                      "You will take turns with your opponent taking 1-4 bells on your turn.\n"
                      "The player to take the last bell loses.")
                print("You are playing against a computer.\n"
                      "The computer will always take the optimal number.\n"
                      "If there is no optimal number, it will choose a random number.")
                print("You can either choose how many bells start in the basket...\n"
                      "...or a pseudorandom number from 16-31 inclusive will be selected.")
                y = True
                return True
            elif choice == "N":
                return True
            else:
                print("Sorry, please print 'Y' or 'N'.")
                return False
        x = False
        while not x: # set the number of bells loop
            choice = input("Would you like to set the starting number of bells yourself? Y/N: ")
            if choice == "Y":
                while self.bells < 15:
                    self.bells = int(input("How many bells do you put in the basket? "))
                return True
            elif choice == "N":
                if not y:
                    print("A pseudorandom number will be generated from 16-31.")
                self.bells = int(random.randrange(16, 32))
                print("There are " + str(self.bells) + " bells in the basket.")
            else:
                print("Sorry, please print 'Y' or 'N'.")
                return False
        print("Alright! Time to begin playing.\n"
              "Are you ready?\n"
              ".\n"
              ".\n"
              ".\n"
              "Not that it matters anyway.")

    def run(self, visual): # handles everything related to the actual functioning of the game
        turn = 1  # manages the turns, odd = player turn, even = computer turn
        NIM.setup(self)
        #code for the game goes here
        print(self.win)


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
    game = NIM()  # initialize the game object.
    wn = Visual() # the screen used for the game
    game.run(wn)  # run the game, passing in the Visual so it can be used.

main()