# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:47:10 2013

@author: rammanur
"""

# implementation of card game - Memory

import simplegui
import random

# cards are logically 50x100 pixels in size
DWIDTH = 50
HEIGHT = 100
NUMRANGE = 8
WIDTH = (DWIDTH * NUMRANGE * 2)

# The shuffled number list
number_list = []

# which cards are exposed
exposedcards = []

# state of cards, False=!identified, True=identified
cardstate = []

# current pair of cards
cardpair = [-1, -1]

# Number of turns taken and current state
turns_taken = 0
state = 0

test_my_code          = 0 # Set to 1 to enable testing mode
print_debug           = 0 # Set to 1 to enable debug prints

# Helper functions

# helper function to print debug msgs when print_debug is set to 1
def debug_print(print_string):
    # This is a debug print function
    # it will generate debug msgs when print_debug is set to 1
    if (print_debug):
        print print_string
        
# helper function to test my code
def test_driver():
    #testing my code
    pass

# helper function to initialize globals
def new_game():
    global state, number_list, exposedcards, cardstate
    global turns_taken
    
    # initialize the card states
    exposedcards = [False] * NUMRANGE * 2
    cardstate = [False] * NUMRANGE * 2
    turns_taken = 0
    state = 0
    cardpair = [-1, -1]
    
    # create the random number list
    number_list = range(0,NUMRANGE) + range(0,NUMRANGE)
    random.shuffle(number_list)
    return

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turns_taken
    global exposedcards, state
    
    # Check which card is clicked and set exposed state
    clickedcard = pos[0]/DWIDTH
    debug_print(("clicked card is ", clickedcard, "state is", state))
    
    # If its an already clicked card, ignore it
    if (exposedcards[clickedcard] == True):
        return
    
    # New card clicked
    # Update the turns taken and state
    if state == 0:
        # Update the needed stuff
        state = 1
        turns_taken += 1 
        cardpair[0] = clickedcard
        exposedcards[clickedcard] = True
    elif state == 1:
        # Update the needed stuff
        state = 2
        cardpair[1] = clickedcard
        exposedcards[clickedcard] = True
    else:    
        # Check if we got a match
        turns_taken += 1 
        card0, card1 = cardpair[0], cardpair[1]
        if (number_list[card0] != number_list[card1]):
            # Turn off the cards displayed so far
            debug_print(("turning off", cardpair[0], cardpair[1]))
            exposedcards[card0] = False
            exposedcards[card1] = False
        
        # Update the new card
        exposedcards[clickedcard] = True
        cardpair[0] = clickedcard
        state = 1

    # Check if we need to (un)expose cards
    # and if there is a match
    return

# Draw the numbers as required
def draw_numbers(canvas):        
    i = 0
    xpos = 0
    
    # Draw the numbers evenly along the canvas in a 
    # somewhat middled fashion and each number gets
    # the same width (divide complete width by number
    # of numbers in the game)
    for x in number_list:
        canvas.draw_text(str(x), [(xpos*DWIDTH+10), \
            HEIGHT-30], HEIGHT-50, "White")
        xpos += 1
    return

def draw_cards(canvas):
    for i in range(NUMRANGE*2):
        x,y = i*DWIDTH, (i+1)*DWIDTH
        if (exposedcards[i] == False):
            canvas.draw_polygon([(x,0), \
                    (y,0), \
                    (y,HEIGHT), \
                    (x, HEIGHT)], \
                    2, 'White', 'Blue')
    return

def draw(canvas):
    global exposedcards, cardstate
    
    # Draw the numbers on the canvas
    draw_numbers(canvas)    
    
    # Update the number of turns taken
    turns_message = "Turns = " + str(turns_taken)
    label.set_text(turns_message)
    
    # Draw the cards
    # cards are logically 50x100 pixels in size
    draw_cards(canvas)
    return

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset/Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric