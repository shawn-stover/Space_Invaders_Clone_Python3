# Imports
import turtle
import os
import math
import random

# Set up the screen
WIDTH, HEIGHT = 600, 600
playWindow = turtle.Screen()
playWindow.setup(WIDTH + 4, HEIGHT + 4)
playWindow.bgcolor('black')
playWindow.title('Space Invaders Clone')

# Draw game border
# border.pen creates a pen to draw 
# penup and pendowncontrol whether the pen is lifted or placed
# fd controls how far the pen moves
# lt turns the pen that many degrees to the left
# speed 0 is as fast as possible

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

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

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

def fire_weapon():
    # Declare weapon state as a global if it needs to be changed
    global weaponstate
    if weaponstate == 'ready':
        weaponstate = 'fire'
        
        # Move bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x, y)
        weapon.showturtle()

def isCollision(turt1, turt2):
    distance = math.sqrt(math.pow(turt1.xcor() - turt2.xcor(),2) + math.pow(turt1.ycor() - turt2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# Create player weapon
weapon = turtle.Turtle()
weapon.color('yellow')
weapon.shape('triangle')
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5, 0.5)
weapon.hideturtle()

weaponspeed = 20

# Define weapon state:

# Ready - Ready to fire weapon
# Fire - Weapon is firing

weaponstate = "ready"

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'd')
turtle.onkey(fire_weapon, 'space')

# Number of enemies
number_of_enemies = 5

# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# Set enemy speed
enemyspeed = 2

# Main Game Loop
while True:

    for enemy in enemies:
        # Move enemy right
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move enemy back opposite direction when border ir reached
        if x > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)
            # Change direction
            enemyspeed *= -1

        if x < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change direction    
            enemyspeed *= -1

        # Check for a collision between the weapon and the enemy
        if isCollision(weapon, enemy):
            # Reset the weapon
            weapon.hideturtle()
            weaponstate = 'ready'
            weapon.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = 'Score: %s' %score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if isCollision(player, enemy):
            # Hide turtles
            player.hideturtle()
            enemy.hideturtle()
            # Print Game Over and break out of game loop
            print('Game Over')
            break
    
    # Move the player weapon
    if weaponstate == "fire":
        y = weapon.ycor()
        y += weaponspeed
        weapon.sety(y)

    # Make sure bullet disappears when it reaches the top of the screen
    if weapon.ycor() > 275:
        weapon.hideturtle()
        weaponstate = 'ready'



# Delay for testing
delay = input('Press Enter or Return to exit.')

