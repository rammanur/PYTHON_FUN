# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:30:34 2013

@author: rammanur
"""

### Implementation of classic arcade game Pong ###

#											
#         ("`-''-/").___..--''"`-._			
#         `6_ 6  )   `-.  (     ).`-.__.`)	
#         (_Y_.)'  ._   )  `._ `. ``-..-'	
#       _..`--'_..-_/  /--'_.' ,'			
#      (il),-''  (li),'  ((!.-'  			
#											

# Import the libraries needed.
import simplegui
import random

# Initialize global variables - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# Initialize ball_pos and ball_vel for new ball in middle of table
# If direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel #These are vectors stored as list.
    
    # Initial values for the ball
    ball_pos = [0, 0]
    ball_vel = [0, 0]
    
    # Spawn the ball at the center of the canvas.
    ball_pos[0] = WIDTH / 2 
    ball_pos[1] = HEIGHT / 2
    
    if direction:
        ball_vel[0] = random.randrange(2, 4) #Ball goes to the right.
    else:
        ball_vel[0] = -random.randrange(2, 4) #Ball goes to the left.
        
    ball_vel[1] = -random.randrange(1, 2) #Adds a little of "upwards velocity".

# Define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  #These are numbers.
    global score1, score2  #These are ints.
    
    # Randomly choice whenever the ball should go to the right or left.
    spawn_ball(random.choice([RIGHT, LEFT]))
    
    score1, score2 = 0, 0
    paddle1_vel, paddle2_vel = 0, 0
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # Play the chiptune song.
    music.play()
    
    # Draw mid line and paddles.
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "#FFF5EE") #Colour - SeaShell
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "#FFF5EE")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "#FFF5EE")
        
    # Update ball.
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # Conditions to make the ball to bounce off the walls.
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] * 1.07
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] * 1.07
    
    # Conditions to make the ball hit the paddles.
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        # If the ball hit the paddle, it bounces and adds a little bit of speed.
        if (paddle1_pos + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] * 1.10
            ball_vel[1] = ball_vel [1] * 1.05
        # If not, player 2 gets a point.
        else:
            score2 = score2 + 1
            spawn_ball(RIGHT)
    
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        # If the ball hit the paddle, it bounces and adds a little bit of speed.
        if (paddle2_pos + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle2_pos-HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] * 1.10
            ball_vel[1] = ball_vel [1] * 1.05
        # If not, player 1 gets a point.
        else:
            score1 = score1 + 1
            spawn_ball(LEFT)
    
    # Draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 4, "#FFF8C6", "#FFF8C6") #Colour - Lemon Chiffon.
    
    # Update paddle's vertical position, keep paddle on the screen.
    if paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    else:
        paddle1_pos = paddle1_pos + paddle1_vel

    if paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    else:
        paddle2_pos = paddle2_pos + paddle2_vel
    
    # Draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "#FFFFFF")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "#FFFFFF")
    
    # Draw scores
    c.draw_text(str(score1), [150, 75], 30, "#FFFFFF") #Colour - White.
    c.draw_text(str(score2), [450, 75], 30, "#FFFFFF")

# Keeps moving the paddle position by 5 pixels as long as the key is held down.
def keydown(key):
    global paddle1_vel, paddle2_vel
    move_pos = 5
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddle1_vel - move_pos
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle1_vel + move_pos
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = paddle2_vel - move_pos
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle2_vel + move_pos

# When the key is released, the position of the paddle doesn't change, remaining the same.
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT) #400 by 600 pixels
frame.set_canvas_background("#151B54") #Set the background to - Midnight Blue.
frame.add_button("New Game!", new_game, 150) #Button to reset the game.
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Load the *.ogg file and set the volume to 75%.
music = simplegui.load_sound("http://upload.wikimedia.org/wikipedia/commons/8/82/Chiptune2.ogg")
music.set_volume(0.75)

# Start frame
new_game()
frame.start()