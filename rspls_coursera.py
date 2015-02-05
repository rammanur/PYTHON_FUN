"""
# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "spock", "paper", "lizard", "scissors" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# And then play the game..


# NOTE: I have written the game so that the case of string
# doesn't matter. Also, negative cases have been tested as
# can be seen at end of program, but commented out.
"""


# All imports go here..
import random


# helper functions
print_debug = 0
def debug_print(print_string):
    # This is a debug print function
    # it will generate debug msgs when print_debug is set to 1
    if (print_debug):
        print print_string
    
def name_to_number(pname):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    # Rock = 0, Paper = 1, Scissors = 2
    # Lizard = 3, Spock = 4
    
    retval = -1
    if (pname.lower() == "rock"):
        retval = 0
    elif (pname.lower() == "spock"):
        retval = 1
    elif (pname.lower() == "paper"):
        retval = 2
    elif (pname.lower() == "lizard"):
        retval = 3
    elif (pname.lower() == "scissors"):
        retval = 4
    else:
        # ideally, this function shouldnt print the msg. Caller should
        retval = -1
        print "Invalid player name '%s'" % pname
    return (retval)

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    name = ""
    if (number == 0):
        name = "rock"
    elif (number == 1):
        name = "spock"
    elif (number == 2):
        name = "paper"
    elif (number == 3):
        name = "lizard"
    elif (number == 4):
        name = "scissors"
    else:
        # ideally, this function shouldnt print the msg. Caller should
        name = ""   
        print "Invalid number '%d'\n" % number

    return (name)
  

def rpsls(player_name): 
    # convert name to player_number using name_to_number
    player_wins, comp_wins, its_a_tie = 0, 0, 0
    
    player_number = name_to_number(player_name)
    if (player_number == -1):
        print "Cannot play game, try again!\n"
        return
    debug_print ("Player chooses %s %d" % (player_name, player_number,))
    print "Player chooses %s" % (player_name,)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    if (comp_name == ""):
        print "!!! Something wrong with my program! Time to debug... !!!\n"
        return


    # compute difference of comp_number and player_number modulo five
    # mod 5 on -1, -2 or 4, 3 result in 4,3 and are on losing side
    # mod 5 on -3, -4 or 2, 1 result in 2, 1 and are on winning side
    # result of 0 for a mod is a tie.
    # use if/elif/else to determine winner
    difference = comp_number - player_number
    if (difference == 0):
        its_a_tie = 1
    else:
        mod_diff = difference % 5
        debug_print ("comp-player diff= %d mod=%d" % (difference, mod_diff))
        if (mod_diff <= 2):
            comp_wins = 1
        else:
            # the diff must be 3 or 4
            player_wins = 1

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    print "Computer chooses %s" % (comp_name,)    
    debug_print ("Computer chooses %s %d" % (comp_name, comp_number,))

    # print results
    if (player_wins):
        print "Player wins!"
    elif (comp_wins):
        print "Computer wins!"
    elif (its_a_tie):
        print "Player and Computer tie!"
    print "\n"
    

# test the code with successful cases first
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# testing negative case
rpsls("rockstar")
rpsls("Spocktheking")
rpsls("paperlizard")
rpsls("scissorshands")

# testing that case doesn't/shouldn't matter
rpsls("ROCK")
rpsls("spock")
rpsls("PaPer")
rpsls("Lizard")
rpsls("SciSSors")