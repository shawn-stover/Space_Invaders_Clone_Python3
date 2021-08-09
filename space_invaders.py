# Imports
import turtle
import os

# Set up the screen
WIDTH, HEIGHT = 600, 600
playWindow = turtle.Screen()
playWindow.setup(WIDTH + 4, HEIGHT + 4)
playWindow.bgcolor('black')
playWindow.title('Space Invaders Clone')

# Draw game border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Set player speed
playerspeed = 15

# Functions for player movement
def move_left():
    # Get player coordinate
    x = player.xcor()
    # Change player position by the value of playerspeed
    x -= playerspeed
    # Check to make sure player stays inside boundaries
    if x < -280:
        x = -280
    # Set player x to the new coordinate
    player.setx(x)

def move_right():
    # Get player coordinate
    x = player.xcor()
    # Change player position by the value of playerspeed
    x += playerspeed
    # Check to make sure player stays inside boundaries
    if x > 280:
        x = 280
    # Set player x to the new coordinate
    player.setx(x) 

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'd')

# Create Enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

# Set enemy speed
enemyspeed = 2

# main Game Loop
while True:
    # Move enemy right
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # Move enemy back opposite direction when border ir reached
    if x > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if x < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

# Delay for testing
delay = input('Press Enter or Return to exit.')

