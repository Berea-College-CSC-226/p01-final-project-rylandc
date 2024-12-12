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
        self.root.minsize(width=300, height=300)
        self.root.maxsize(width=300, height=300)
        self.root.title("Game of NIM")

        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1 = None
        self.labeltext = tk.StringVar()

        self.bells = 0
        self.win = ""
    
    def game_setup(self):
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
                # print("THE INSTRUCTIONS HAVE PRINTED.")
                y = True
                instruction_loop = False
            elif choice == "N":
                # print("THE INSTRUCTIONS WILL NOT BE PRINTED.")
                instruction_loop = False
            else:
                print("Sorry, please print 'Y' or 'N'.")
                instruction_loop = True
        # print("THE WHILE LOOP HAS BEEN EXITED.")
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
        print("Alright! Time to begin playing.\n"
              "Are you ready?\n"
              ".\n"
              ".\n"
              ".\n"
              "Not that it matters anyway.")

    def wn_setup(self):
        self.create_button1()
        self.create_textbox1()
        self.create_label1()
        self.game_setup()

    def create_button1(self):
        self.myButton1 = tk.Button(self.root, text="Take bells", command=self.button1_handler)
        self.myButton1.grid(row=0, column=0) # top of the window

    def create_textbox1(self):
        self.myTextBox1.grid(row=1, column=0) # middle of the window

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
        """
        The label below the textbox is the number of bells; this method sets that up.

        """
        labeltext = str(self.bells)
        self.labeltext.set(value= labeltext)
        self.myTextLabel1 = tk.Label(self.root, textvariable= self.labeltext)
        self.myTextLabel1.grid(row=2, column=0) # bottom of the window

    def button1_handler(self):
        """
        Event handler for button1 above.
        Takes the input number of bells (if within acceptable range) and subtracts it from total.
        Checks first to make sure it is a number from 1-4 inclusive.

        """
        text = self.myTextBox1.get()
        text = int(text)
        #print(type(text))
        if 1 <= text <= 4:  # if the number entered is between 1 and 4 inclusive
            self.bells -= text
            print(self.bells)
            comp_turn = True
            if self.bells <= 1:
                pass

        else:
            print("Whoops! Invalid entry!")
        
        if comp_turn:
            five = 5 - (self.bells % 5)
            # print(type(bells))
            if five == 5 or five == 0:
                take = int(random.randrange(1, 5))
            else:
                take = int(five)
            # print(type(take))
            self.bells -= take
            print(self.bells)



# Section 2: The main() stuff.

def main():
    """
    Creates an object of the Game class and begins the game.

    """
    wn = Game() #
    wn.wn_setup()
    wn.root.mainloop()

main()