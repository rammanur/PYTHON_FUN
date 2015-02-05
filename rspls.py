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
"""

# helper functions



import random

rock, papers, scissors, lizard, spock = range(5)
rps_names = ["rock", "spock", "paper", "lizard", "scissors"]

# Alternate helper functions
def number_to_name_alternate(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    len = rps_names.__len__()
    if (number < 0):
        return rps_names[len]
    if (number >= len):
        return rps_names[len]
    return (rps_names[number])

def name_to_number_alternate(name):
    # Converts given name to number
    # Rock = 0, Paper = 1, Scissors = 2
    # Lizard = 3, Spock = 4
    if name.lower() in rps_names:
        return rps_names.index(name)
    else:
        return (-1)

# helper functions

def number_to_name(number):
    # fill in your code below
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
        name = ""        
    return (name)
  
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    # Rock = 0, Paper = 1, Scissors = 2
    # Lizard = 3, Spock = 4
    retval = -1
    if (name.lower() == "rock"):
        retval = 0
    elif (name.lower() == "spock"):
        retval = 1
    elif (name.lower() == "paper"):
        retval = 2
    elif (name.lower() == "lizard"):
        retval = 3
    elif (name.lower() == "scissors"):
        retval = 4
    else:
        retval = -1
    return (retval)

print_debug = 0
def debug_print(print_string):
    if (print_debug):
        print print_string
    
def rpsls(player_name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_wins, comp_wins, its_a_tie = 0, 0, 0
    
    player_number = name_to_number(player_name)
    if (player_number == -1):
        return
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    debug_print ("Player chooses %s %d" % (player_name, player_number,))
    print "Player chooses %s" % (player_name,)


    # compute difference of player_number and comp_number modulo five
    difference = (comp_number - player_number) % 5
    #print "comp-player diff= %d" % (difference,)    
   
    # use if/elif/else to determine winner
    if (difference == 0):
        its_a_tie = 1
    elif (difference == 1 or difference == 2):
        comp_wins = 1
    else:
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
        print "Its a tie!"
    print "\n"
    
      
    
# always remember to check your completed program against the grading rubric

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
