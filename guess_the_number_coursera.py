# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 05:25:16 2013

@author: rammanur
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

"""

import simplegui
import math
import random

# initialize global variables used in your code
message                   = 'Guess the number game!'
low, high                 = 0, 100
number_of_guesses         = 0
random_secret_number      = 0
previous_guess            = high/2
number_of_guesses_allowed = math.ceil(math.log(high, 2))

# Helper functions

# helper function to print debug msgs when print_debug is set to 1
print_debug = 0 
def debug_print(print_string):
    # This is a debug print function
    # it will generate debug msgs when print_debug is set to 1
    if (print_debug):
        print print_string

# Helper function to help calculate a good guess
def get_diff(previous_guess, user_guess):
    if (previous_guess == user_guess):
        diff = float(previous_guess)/2
    elif (previous_guess < user_guess):
        diff = float(user_guess-previous_guess)/2
    else:
        diff = float(previous_guess-user_guess)/2
    if (diff == 0):
        diff = 1
    diff = math.ceil(diff)
    return int(diff)
        
# Helper function to start and restart the game
def new_game():
    # reset the global variables
    global number_of_guesses_allowed
    global random_secret_number
    global number_of_guesses
    global previous_guess

    number_of_guesses         = 0
    number_of_guesses_allowed = math.ceil(math.log(high, 2))
    random_secret_number      = random.randrange(low, high)
    previous_guess            = high/2

    print("\nNew game. Range is from 0 to %d" % (high,))
    print("Number of remaining guesses is %d" % number_of_guesses_allowed)
    debug_print("new_game(): Computer selected number=%d, #guesses=%d" % (random_secret_number, number_of_guesses))
    
    return

# define event handlers for control panel
def input_guess(users_input):
    # main game logic goes here	
    global number_of_guesses
    global number_of_guesses_allowed
    global previous_guess

    number_of_guesses += 1
    user_guess = int(users_input)
    print "\nGuess was %d" % (user_guess,)
    debug_print("input_guess(): You guessed(%d)=%d secret=%d" % (number_of_guesses, user_guess, random_secret_number))
    if (user_guess < 0 or user_guess >= high):
        print "Invalid guess: should be (0-%d], please play again!" % high
        new_game()
        return
    
    rem_guesses = number_of_guesses_allowed - number_of_guesses
    print "Number of remaining guesses is %d" % (rem_guesses)
    
    # Guessed it ?
    if (user_guess == random_secret_number):
        print "Correct!"
        new_game()
        return

    # done with all allowed guesses ?
    if (rem_guesses == 0):
        print "You ran out of guesses. The number was %d. Play again!" %    (random_secret_number, number_of_guesses_allowed,)
        new_game()
        return
    
    #Higher or lower ?
    diff = get_diff(previous_guess, user_guess)
    if (user_guess < random_secret_number):
        print "Higher!"
        good_guess = user_guess + diff
        debug_print("p=%d u=%d good guess would be %d" % (previous_guess, user_guess, good_guess))
    else :              
        print "Lower!"
        good_guess = user_guess - diff
        debug_print("p=%d u=%d good guess would be %d" % (previous_guess, user_guess, good_guess))

    previous_guess = user_guess    
    return    

def range100():
    # button that changes range to range [0,100) and restarts
    global high
    
    high = 100
    new_game()    
    return

def range1000():
    # button that changes range to range [0,1000) and restarts
    global high
    
    high = 1000
    new_game()    
    return

# Handler to draw on canvas
def draw_handler(canvas):
    canvas.draw_text(message, [50,112], 30, "Blue", 'monospace')
    return

# create frame
frame = simplegui.create_frame("Home", 500, 200)
button100 = frame.add_button("Range is [0 - 100)", range100, 200)
button1000 = frame.add_button("Range is [0 - 1000)", range1000, 200)
inpbox = frame.add_input('Enter a Guess', input_guess, 200)
frame.set_draw_handler(draw_handler)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric