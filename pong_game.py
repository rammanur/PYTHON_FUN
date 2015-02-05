# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH                 = 600
HEIGHT                = 400       
BALL_RADIUS           = 20
PAD_WIDTH             = 8
PAD_HEIGHT            = 80
HALF_PAD_WIDTH        = PAD_WIDTH / 2
HALF_PAD_HEIGHT       = PAD_HEIGHT / 2
LEFT                  = False
RIGHT                 = True
MESSAGE               = "PONG GAME"

paddle1_pos           = [HEIGHT/2-HALF_PAD_HEIGHT, \
                         HEIGHT/2-HALF_PAD_HEIGHT+PAD_HEIGHT]
paddle2_pos           = list(paddle1_pos)
ball_pos              = [WIDTH / 2, HEIGHT / 2]
initial_ball_velocity = [2, -2]
hball_velocity        = list(initial_ball_velocity)
direction             = RIGHT
start_button          = False
score_left            = 0 # Left side player score
score_right           = 0 # Right side player score

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
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else 
# upper left
def spawn_ball(direction):
    global ball_pos # these are vectors stored as lists
    global score_left, score_right
    global hball_velocity
    
    # Reset the values
    hrandomizer = 0
    vrandomizer = 0
    ball_pos          = [WIDTH / 2, HEIGHT / 2]
    hball_velocity     = list(initial_ball_velocity)
    hrandomizer       = random.randrange(120, 240)
    vrandomizer       = random.randrange(60, 180)
    #hball_velocity[0] *= hrandomizer
    #hball_velocity[1] *= vrandomizer
    
    # Fix the direction correctly
    if (direction):
        hball_velocity[0] = -hball_velocity[1]
        hball_velocity[1] = -hball_velocity[0]
    else:
        hball_velocity[0] = hball_velocity[1]
        hball_velocity[1] = hball_velocity[0]
        
    debug_print(("In SPAWN", ball_pos[0], ball_pos[1], hrandomizer, vrandomizer, \
        hball_velocity[0], hball_velocity[1]))
    
# define event handlers
def new_game():
    #Start a new game
    global paddle1_pos, paddle2_pos # these are numbers
    global paddle1_vel, paddle2_vel # these are numbers
    global score_left, score_right  # these are ints
    global direction, start_button

    debug_print(("In new_game"))
    
    # Initialize the scores
    score_left        = 0
    score_right       = 0
    
    #Call spawn_ball
    direction = RIGHT
    spawn_ball(direction)
    
    debug_print(("P1-0, P1-1, P2-0, P2-1 =", paddle1_pos[0], paddle1_pos[0], \
                paddle2_pos[0], paddle2_pos[1]))

def update_ball_pos():
    # update ball
    global hball_velocity
    global score_left, score_right
    global direction
    global paddle1_pos, paddle2_pos # these are numbers
    
    # Dont change position if game is not in play
    if (start_button == False):
        return

    # did ball hit the gutter on left hand side of canvas
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)):
        debug_print ("ball pos[1] when hit left wall is %d" % \
               ball_pos[1])
        if (ball_pos[1] > paddle1_pos[0] and ball_pos[1] \
            <= paddle1_pos[1]):
            # Increase the speed of the ball by 10%
            temp =  ((hball_velocity[0]*10)/100)            
            hball_velocity[0] += temp           
            hball_velocity[0] = -hball_velocity[0]
        else:
            #update score and Call spawn_ball
            score_right += 1
            direction = RIGHT
            spawn_ball(direction)
            return
        
    # did ball hit the gutter on right hand side of canvas
    elif (ball_pos[0] >= (WIDTH-1-BALL_RADIUS-PAD_WIDTH)):
        debug_print ("ball pos[1] when hit right wall is %d" % \
               ball_pos[1])        
        debug_print ("p2[0]=%d p2[1]=%d" % \
               (paddle2_pos[0], paddle2_pos[1],))
        if (ball_pos[1] > paddle2_pos[0] and ball_pos[1] <= paddle2_pos[1]):
            # Increase the speed of the ball by 10%
            temp = -((hball_velocity[0]*10)/100)
            hball_velocity[0] += temp
            hball_velocity[0] = -hball_velocity[0]
        else:
            #update score and call spawn ball
            score_left += 1
            direction = LEFT
            spawn_ball(direction)
            return

    # collide and reflect off of bootom side of canvas
    elif (ball_pos[1] >= (HEIGHT-1-BALL_RADIUS)):
        hball_velocity[1] = - hball_velocity[1]

    # collide and reflect off of top side of canvas
    elif (ball_pos[1] <= BALL_RADIUS):
        hball_velocity[1] = - hball_velocity[1]
        
    ball_pos[0] += hball_velocity[0]
    ball_pos[1] += hball_velocity[1]
    debug_print (("ball pos [0]=%d [1]=%d" % (ball_pos[0], ball_pos[1])))

# Event handler for start button
def startb_hdlr():
    # start button handler
    global start_button
    start_button = True

# Event handler for stop button
def stopb_hdlr():
    # stop button handler
    global start_button
    start_button = False
 
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
# Key handler
def keyhandler(key):
    global paddle1_pos, paddle2_pos
    
    # Lets use a velocity of 40
    local_vel = 40
    if (key == simplegui.KEY_MAP["down"]):
        paddle2_pos[0] += local_vel
        paddle2_pos[1] += local_vel
    elif (key == simplegui.KEY_MAP["up"]):
        paddle2_pos[0] -= local_vel
        paddle2_pos[1] -= local_vel
        
    if (key == simplegui.KEY_MAP['s']):
        paddle1_pos[0] += local_vel
        paddle1_pos[1] += local_vel
    elif (key == simplegui.KEY_MAP['w']):
        paddle1_pos[0] -= local_vel
        paddle1_pos[1] -= local_vel
        debug_print(("p1 pos[0]=%d pos[1]=%d" % paddle1_pos[0], paddle1_pos[1]))

    if (paddle1_pos[0] <= 0):
        debug_print(("pad1 pos: 0: %d" % paddle1_pos[0]))
        paddle1_pos[0] = 0
        paddle1_pos[1] = PAD_HEIGHT
    elif(paddle1_pos[1] >= HEIGHT):
        debug_print(("pad1 pos: 0: %d" % paddle1_pos[1]))
        paddle1_pos[0] = HEIGHT-PAD_HEIGHT
        paddle1_pos[1] = HEIGHT
    if (paddle2_pos[0] <= 0):
        debug_print(("pad2 pos: 0: %d" % paddle2_pos[0]))
        paddle2_pos[0] = 0
        paddle2_pos[1] = PAD_HEIGHT
    elif(paddle2_pos[1] >= HEIGHT):
        debug_print(("pad2 pos: 1: %d" % paddle2_pos[1]))
        paddle2_pos[0] = HEIGHT-PAD_HEIGHT
        paddle2_pos[1] = HEIGHT

def draw(c):
    global score_left, score_right
    global paddle1_pos, paddle2_pos
    global ball_pos
    
    c.draw_text(MESSAGE, [WIDTH/2-180,HEIGHT], 80, "Black", 'monospace')

        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        

    # draw paddles
    c.draw_line([0, paddle1_pos[0]],[0, paddle1_pos[1]], PAD_WIDTH*2, "Orange")
    c.draw_line([WIDTH, paddle2_pos[0]],[WIDTH, paddle2_pos[1]], PAD_WIDTH*2, "Red")

    # draw scores
    c.draw_text(str(score_left), [WIDTH/4, 50], 40, "Black", 'monospace')
    c.draw_text(str(score_right), [WIDTH/2+WIDTH/4, 50], 40, "Black", 'monospace')

    # update ball position and draw ball
    update_ball_pos()
    c.draw_circle(ball_pos, BALL_RADIUS, 8, "Green", "Yellow")
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Blue')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyhandler)
new_gameb = frame.add_button("Restart New Game", new_game, 200)
startb = frame.add_button("Start/Continue Game", startb_hdlr, 200)
stopb = frame.add_button("Stop Game", stopb_hdlr, 200)


#music
music = simplegui.load_sound("http://upload.wikimedia.org/wikipedia/commons/8/82/Chiptune2.ogg")
music.set_volume(0.75)


# start frame
new_game()
frame.start()
