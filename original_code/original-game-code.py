import random

def game(bells):
    """
    Runs the majority of the game.

    :param bells: The number of bells in the basket.
    :return: x; how many turns have passed, used to calculate winner.
    """
    turn = 1
    print(type(bells))
    win = ""
    while bells > 0:
        print("t. " + str(turn))
        print(type(turn))
        print("There are " + str(bells) + " bells in the basket.")
        if turn % 2 == 1:
            bells = human_plays(bells)
        else:
            bells = comp_plays(bells)
        turn = turn + 1
    return turn


def human_plays(bells):
    """
    When it's the player's turn, asks them how many bells they want to take and takes
    that number of bells from the basket.

    :param bells: How many bells are in the basket.
    :return: bells; the number of bells remaining in the basket.
    """
    print(type(bells))
    take = int(input("How many bells do you take? "))
    print(type(take))
    bells = bells - take
    return bells


def comp_plays(bells):
    """
    When it's the computer's turn, calculates the optimal number of bells to take.
    If there is no optimal number, takes random amount of bells from 1-4 inclusive.

    :param bells: How many bells are in the basket.
    :return: bells; the number of bells remaining in the basket.
    """
    five = 5 - (bells % 5)
    #print(type(bells))
    take = 0
    if five == 5 or five == 0:
        take = int(random.randrange(1, 5))
    else:
        take = int(five)
    #print(type(take))
    bells = bells - take
    return bells


def main():
    """
    Sets the number of bells, runs the game function, and calculates the winner.

    """
    bells = 0
    while bells < 15:
        bells = int(input("How many bells do you put in the basket? "))
    turn = game(bells)
    if turn % 2 == 1:
        win = "The computer "
    else:
        win = "You "
    print(win + "won!")


main()