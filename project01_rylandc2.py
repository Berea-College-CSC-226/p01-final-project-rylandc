######################################################################
# Author: Charle Ryland
# Username: rylandc
#
# Purpose:
# To run the Game of NIM with a (simple) GUI.
######################################################################
# Acknowledgements:
# I consulted the TA, Nicholas, to figure out how to get the classes to interact the way I need them to.
#
#
#
######################################################################
import tkinter as tk
import random


# Section 1: The GUI and game logic stuff.

class Game:
    """
    Responsible for everything GUI.

    """
    def __init__(self):
        """
        The initializer instantiates a window for the widgets.

        """
        self.root = tk.Tk()
        self.root.minsize(width=250, height=80) # the required size to see everything
        self.root.maxsize(width=300, height=300)
        self.root.title("Game of NIM")

        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1 = None
        self.labeltext = tk.StringVar() # this label will show the number of bells
        self.win_label = tk.StringVar() # this label will display the win/lose message

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
        print("Alright! Time to begin playing.")


    def wn_setup(self):
        """
        Sets the game and window up.

        """
        self.create_button1()
        self.create_textbox1()
        self.game_setup() # the label will be created once self.bells is set to not-zero


    def create_button1(self):
        """
        Creates a button in the top left of the window.

        """
        self.myButton1 = tk.Button(self.root, text="Take bells", command=self.button1_handler)
        self.myButton1.grid(row=0, column=0) # top of the window


    def create_textbox1(self):
        """
        Creates a textbox in the middle left of the window.

        """
        self.myTextBox1.grid(row=1, column=0)


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


    def comp_plays(self, test):
        """
        Manages the actions of the computer on its turn.

        :param test: only True if the method is being called in the testing method
        :return: test_c is a testing variable intended for use in the test suite only.
        """
        five = 5 - (self.bells % 5) # how many bells to the next multiple of five
        if five == 5 or five == 0: # if there is a multiple of five in the basket
            take = int(random.randrange(1, 5))
        else:
            take = int(five) # else, take the optimal number
        if (self.bells - take) < 0: # if take would put the bells into the negative
            take = self.bells # then just take all the bells and no more
        self.bells -= take
        test_c = True
        if not test: # if this is not a test
            self.create_label1()
        if self.bells < 1: # if computer took the last bell
            self.win = "You won!" # then you won
            if not test:
                self.create_win_label()
            test_c = False
        return test_c


    def human_plays(self, text, test):
        """
        Manages the game logic that occurs on the player's turn.

        :param text: The number entered into the textbox.
        :param test: only True if the method is being called in the testing method
        :return: test_h is a testing variable intended for use in the test suite only.
        """
        self.bells -= text
        test_h = None
        if self.bells >= 1: # if you did not take the last bell
            if not test: # if this is not a test
                self.create_label1() # the game continues
            test_h = True
        elif self.bells < 1: # if you took the last bell
            self.win = "You lost!" # then you lost
            if not test:
                self.create_win_label()
            test_h = False
        return test_h


    def button1_handler(self):
        """
        Event handler for button1 above.
        Takes the input number of bells (if within acceptable range) and subtracts it from total.
        Checks first to make sure it is a number from 1-4 inclusive.

        """
        if self.bells > 0: # if there are any bells in the basket
            text = int(self.myTextBox1.get())
            if 1 <= text <= 4:  # if the number entered is between 1 and 4 inclusive
                self.human_plays(text)
                if self.bells > 0: # check again so comp_plays() doesn't happen if player already won
                    self.comp_plays()
        # button does nothing if game has concluded or an invalid number is input


    def test_human_plays(self, bells, text):
        """
        Intended for use in the test suite only. Do not run in main program.
        Tests the human_plays() method.
        test_h is True if the game would continue, False if it ends.

        :param bells: Number of bells to start
        :param text: Number of bells to be taken
        """
        self.bells = bells
        test = True
        test_h = self.human_plays(text, test)
        if test_h:
            print("Game continues, " + str(self.bells))
        else:
            print("Game ends, " + str(self.bells))


    def test_comp_plays(self, bells):
        """
        Intended for use in the test suite only. Do not run in main program.
        Tests the comp_plays() method.
        test_c is True if the game would continue, False if it ends.

        :param bells: Number of bells to start
        """
        self.bells = bells
        test = True
        test_c = self.comp_plays(test)
        if test_c:
            print("Game continues, " + str(self.bells))
        else:
            print("Game ends, " + str(self.bells))



# Section 2: The main() stuff.

def main():
    """
    Creates an object of the Game class and begins the game.

    """
    wn = Game()
    wn.wn_setup()
    wn.root.mainloop()

if __name__ == "__main__":
    main()