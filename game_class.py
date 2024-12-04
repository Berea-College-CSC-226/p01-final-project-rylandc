import random

class NIM:
    def __init__(self):
        """
        The initializer establishes variables used in all the methods.

        """
        self.bells = 0 # number of bells in the basket currently
        self.win = "Game not played."  # wrong string right now, will later be set to winner message
        self.setup()

    def human_turn(self):
        pass

    def comp_turn(self):
        pass

    def setup(self):
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
                print("THE INSTRUCTIONS HAVE PRINTED.")
                y = True
                instruction_loop = False
            elif choice == "N":
                print("THE INSTRUCTIONS WILL NOT BE PRINTED.")
                instruction_loop = False
            else:
                print("Sorry, please print 'Y' or 'N'.")
                instruction_loop = True
        print("THE WHILE LOOP HAS BEEN EXITED.")
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

    def win_message(self):
        return self.win

    def run(self, visual): # handles everything related to the actual functioning of the game
        turn = 1  # manages the turns, odd = player turn, even = computer turn
        NIM.setup(self)
        #code for the game goes here
        print(self.win)