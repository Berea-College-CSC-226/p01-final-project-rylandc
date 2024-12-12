######################################################################
# Author: Charle Ryland
# Username: rylandc
#
# Purpose:
# To test the project01_rylandc2.py file for possible issues.
######################################################################
import project01_rylandc2 as project

test_game = project.Game()

# False = game ends, True = game continues

# test the comp_plays method (self, bells)
# should end if computer takes last bell
print("This test should be be 'Game ends':")
test_game.test_comp_plays(1)
# should continue if computer can force player to take last bell (4 tests)
print("These tests should be 'Game continues':")
test_game.test_comp_plays(2) # this test fails. All others pass. Error is found and accounted for.
test_game.test_comp_plays(3)
test_game.test_comp_plays(4)
test_game.test_comp_plays(5)
# should continue if computer cannot force the game to end (2 tests)
print("These tests should be 'Game continues':")
test_game.test_comp_plays(7)
test_game.test_comp_plays(9)

# test the human_plays method (self, bells, text)
# should end if player takes last bell
print("These tests should be be 'Game ends':")
test_game.test_human_plays(1, 1)
test_game.test_human_plays(2, 2)
# should continue if player does not take last bell
print("These tests should be 'Game continues':")
test_game.test_human_plays(10, 3)
test_game.test_human_plays(7, 2)