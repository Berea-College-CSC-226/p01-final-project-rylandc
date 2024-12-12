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
import random


# Section 1: The GUI stuff.

class Game:
    """
    Responsible for everything GUI.

    """
    def __init__(self):
        """
        The initializer instantiates a window for the widgets.

        """
        self.root = tk.Tk()
        self.root.minsize(width=250, height=80)
        self.root.maxsize(width=300, height=300)
        self.root.title("Game of NIM")

        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1 = None
        self.labeltext = tk.StringVar()
        self.win_label = tk.StringVar()

        self.bells = 0
        self.win = ""


    def game_setup(self):
        """
        Offers to explain how to play the game.
        Sets up the number of bells.

        """
        print("Welcome to the Game of NIM!")
        y = False  # this is to determine if the random bells instruction is needed.
        instruction_loop = True
        while instruction_loop:  # true = player answered, exit the loop, false = need to ask again
            choice = input("Do you need instructions? Y/N: ")
            if choice == "Y":
                print("In this game, there is a basket of 16 or more bells.\n"
                      "You will take turns with your opponent taking 1-4 bells on your turn.\n"
                      "The player to take the last bell loses.\n"
                      "Therefore, the goal of this game is to leave only 1 bell for your opponent to take.")
                print("You are playing against a computer.\n"
                      "The computer will always take the optimal number.\n"
                      "If there is no optimal number, it will choose a random number.")
                print("You can either choose how many bells start in the basket...\n"
                      "...or a pseudorandom number from 16-31 inclusive will be selected.")
                y = True
                instruction_loop = False
            elif choice == "N":
                instruction_loop = False
            else:
                print("Sorry, please print 'Y' or 'N'.")
                instruction_loop = True
        bells_loop = True
        while bells_loop:  # set the number of bells loop
            choice = input("Would you like to set the starting number of bells yourself? Y/N: ")
            if choice == "Y":
                while self.bells < 15:
                    self.bells = int(input("How many bells do you put in the basket? "))
                bells_loop = False
            elif choice == "N":
                if not y:
                    print("A pseudorandom number will be generated from 16-31.")
                self.bells = int(random.randrange(16, 32))
                print("There are " + str(self.bells) + " bells in the basket.")
                bells_loop = False
            else:
                print("Sorry, please print 'Y' or 'N'.")
                bells_loop = True
        self.create_label1()
        print("Alright! Time to begin playing.\n"
              "Are you ready?\n"
              ".\n"
              ".\n"
              ".\n"
              "Not that it matters anyway.")


    def wn_setup(self):
        self.create_button1()
        self.create_textbox1()
        self.game_setup()


    def create_button1(self):
        self.myButton1 = tk.Button(self.root, text="Take bells", command=self.button1_handler)
        self.myButton1.grid(row=0, column=0) # top of the window


    def create_textbox1(self):
        self.myTextBox1.grid(row=1, column=0) # middle of the window


    def create_label1(self):
        """
        The label below the textbox is the number of bells; this method sets that up.

        """
        labeltext = str(self.bells)
        self.labeltext.set(value= labeltext)
        self.myTextLabel1 = tk.Label(self.root, textvariable= self.labeltext)
        self.myTextLabel1.grid(row=2, column=0) # bottom of the window


    def create_win_label(self):
        """
        Creates a label to declare the winner when the number of bells drops to 0.

        """
        win_text = str(self.win)
        self.win_label.set(value= win_text)
        self.win_label = tk.Label(self.root, textvariable=self.win_label)
        self.win_label.grid(row=2, column=1)  # right of the window


    def comp_plays(self, text):
        five = 5 - (self.bells % 5)
        if five == 5 or five == 0:
            take = int(random.randrange(1, 5))
        else:
            take = int(five)
        self.bells -= take
        self.create_label1()
        if self.bells <= 1:
            self.win = "You won!"
            self.create_win_label()


    def human_plays(self, text):
        if 1 <= text <= 4:  # if the number entered is between 1 and 4 inclusive
            self.bells -= text
            if self.bells >= 1:
                self.create_label1()
                comp_turn = True
            elif self.bells < 1:
                self.win = "You lost!"
                self.create_win_label()
        else:
            print("Whoops! Invalid entry!")


    def button1_handler(self):
        """
        Event handler for button1 above.
        Takes the input number of bells (if within acceptable range) and subtracts it from total.
        Checks first to make sure it is a number from 1-4 inclusive.

        """
        text = self.myTextBox1.get()
        text = int(text)
        comp_turn = False
        self.human_plays(text)
        if comp_turn:
            self.comp_plays(text)



# Section 2: The main() stuff.

def main():
    """
    Creates an object of the Game class and begins the game.

    """
    wn = Game() #
    wn.wn_setup()
    wn.root.mainloop()

main()