import turtle
import os

wn = turtle.Screen()             #open a screen
wn.title("Pong")                 #set title as pong
wn.bgcolor("black")              #background color set as black
wn.setup(width=800, height=600)  #set the screen area
wn.tracer(0)

# Score
score_a = 0           #Initialise scores
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()                      #Initialise paddle a as a Turtle
paddle_a.speed(0)                               #Set starting speed of paddle a as zero
paddle_a.shape("square")                        #Set shape of paddle a
paddle_a.color("white")                        #color of paddle a
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #Set the size of sides of the square to become a rectangle
paddle_a.penup()                                #do penup so not to leave a trail behind the paddle
paddle_a.goto(-350, 0)                          #set position of paddle a to left side, using coordinates                                                  
                                                                                    
# Paddle B
paddle_b = turtle.Turtle()                   #All setting same as paddle a, except coordinates are there to set it to right
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  #first six settings similar to paddles, except shape, size and coordinates
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2            #Set speed in x direction to 2
ball.dy = 2            #set speed to 2 for Y axis

# Pen used for displaying points
pen = turtle.Turtle() 
pen.speed(0)             #almost all setting mentioned above
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle() #hide the pen(turtle) as it is not required in the game
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) # set formatting settings for writing through the pen

# Functions
def paddle_a_up():       #function to move paddle a up, using coordinates and changing them
    y = paddle_a.ycor()    #get the coordinates paddle a
    y += 20                #add 20 to it's coordinates
    paddle_a.sety(y)       #set coordinates to updated value of y

def paddle_a_down():    #similar function, but to move paddle a down     
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():          #similar to paddle a
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():        #similar to paddle a
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()                     #tell program to expect input
wn.onkeypress(paddle_a_up, "w")      #move paddle a up when w is pressed
wn.onkeypress(paddle_a_down, "s")    #move paddle a down when s is pressed
wn.onkeypress(paddle_b_up, "Up")     #move paddle b up when up arrow is pressed
wn.onkeypress(paddle_b_down, "Down") #move paddle b down when down arrow is pressed

# Main game loop
while True:    #infinite loop
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #move ball by seeing speed and coordinates, and changing them
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:   #check if ball is hitting top 
        ball.sety(290)      #set ball y coordinate to 290
        ball.dy *= -1       #reverse ball direction
        
    
    elif ball.ycor() < -290:  #reverse of previous condition
        ball.sety(-290)
        ball.dy *= -1
       

    # Left and right
    if ball.xcor() > 350:         #check if ball is hitting left boundary
        score_a += 1              # add 1 to score of a
        pen.clear()               #clear pen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # write score of player 1, by removing previous value of
        #score a and writing new value
        ball.goto(0, 0)        # set ball location to centre
        ball.dx *= -1          #reverse ball direction

    elif ball.xcor() < -350:     #similar code, for player b
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
