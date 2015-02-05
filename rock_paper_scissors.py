# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:53:38 2013

@author: rammanur

Rock-paper-scissors template


The key idea of this program is to equate the strings
"rock", "paper", "scissors" to numbers
as follows:

0 - rock
1 - paper
2 - scissors
"""

import random

rock, papers, scissors = range(3)
rps_names = ["rock", "paper", "scissors"]

rock, papers, scissors = range(3)
rps_names = ["rock", "paper", "scissors", ""]

# v2 helper functions
def number_to_name_v2(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    len = rps_names.__len__()
    if (number < 0):
        return rps_names[len]
    if (number >= len):
        return rps_names[len]
    return (rps_names[number])


def name_to_number_v2(name):
    # Converts given name to number
    # Rock = 0, Paper = 1, Scissors = 2
    if name in rps_names:
        return rps_names.index(name)
    else:
        return (-1)

# v1 helper functions
def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    name = ""
    if (number == 0):
        name = "rock"
    elif (number == 1):
        name = "paper"
    elif (number == 2):
        name = "scissors"
    else:
        name = ""        
    return (name)
    
def name_to_number(name):
    # Converts given name to number
    # Rock = 0, Paper = 1, Scissors = 2
    retval = -1
    if (name == "rock"):
        retval = 0
    elif (name == "paper"):
        retval = 1
    elif (name == "scissors"):
        retval = 2
    else:
        retval = -1
    return (retval)

def rps(player_name): 
    # convert name to player_number using name_to_number
    player_wins, comp_wins = 0, 0
    
    player_number = name_to_number(player_name)
    if (player_number == -1):
        return
    print "Player chooses %s" % (player_name,)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 3)
    
    # compute difference of player_number and comp_number modulo five
    difference = comp_number - player_number 
    
    # use if/elif/else to determine winner
    #if (difference == 1 or difference == -2):
    #    comp_wins = 1
    #elif (difference == -1 or difference == 2):
    #    player_wins = 1
    if (comp_number == player_number):    
        player_wins = 1
    elif (comp_number > player_number || )

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    print "Computer chooses %s" % (comp_name,)    
    
    # print results
    if (player_wins):
        print "Player wins!"
    elif (comp_wins):
        print "Computer wins!"
    else:
        print "Its a tie!"
    print "\n"
    
# test your code
rps("rock")
rps("paper")
rps("scissors")
rps("rock")
rps("paper")
rps("scissors")

# always remember to check your completed program against the grading rubric
