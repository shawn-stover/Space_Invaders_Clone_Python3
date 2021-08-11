# Imports
import turtle
import os
import math
import platform

# if on Windows, import winsound
if platform.system() == 'Windows':
    import winsound


# Set up the screen
WIDTH, HEIGHT = 600, 600
playWindow = turtle.Screen()
playWindow.setup(WIDTH + 4, HEIGHT + 4)
playWindow.bgcolor('black')
playWindow.title('Space Invaders Clone')
playWindow.bgpic('star_background.gif')
playWindow.tracer(0)

# Register the shapes for player, laser and enemy
playWindow.register_shape('space_invader.gif')
playWindow.register_shape('ship.gif')

# Draw game border
# border.pen creates a pen to draw
# penup and pendown control whether the pen is lifted or placed
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

# Set level to 1
level = 1

# Draw the level number
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color('white')
level_pen.penup()
level_pen.setposition(230, 280)
levelstring = 'Level: {}'.format(level)
level_pen.write(levelstring, False, align='left', font=('Arial', 14, 'normal'))
level_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: {}'.format(score)
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# Create the player
player = turtle.Turtle()
player.shape('ship.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

# Functions for player movement

def move_left():
    player.speed = -3


def move_right():
    player.speed = 3


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


def fire_weapon():
    # Declare weapon state as a global if it needs to be changed
    global weaponstate
    if weaponstate == 'ready':
        play_sound('shoot.wav')

        # Set weaponstate to fire when fired
        weaponstate = 'fire'

        # Move bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x, y)
        weapon.showturtle()


def isCollision(turt1, turt2):
    distance = math.sqrt(math.pow(turt1.xcor() - turt2.xcor(), 2) + math.pow(turt1.ycor() - turt2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


def play_sound(sound_file, time=0):
    # Windows
    if platform.system == 'Windows':
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system == 'Linux':
        os.system('aplay -q {}&'.format(sound_file))
    # Mac
    else:
        os.system('afplay -q {}&'.format(sound_file))

    # Repeat sound, used for bgm
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))

# Number of enemies
number_of_enemies = 30

# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.shape('space_invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (40 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy_number
    enemy_number += 1

    # Create rows, using modulo
    if enemy_number == 10:
        enemy_start_x = -225
        enemy_start_y -= 50
        enemy_number = 0

# Set enemy speed
enemyspeed = 0.2

# Create player weapon
weapon = turtle.Turtle()
weapon.color('yellow')
weapon.shape('triangle')
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5, 0.5)
weapon.hideturtle()

weaponspeed = 7

# Define weapon state:

# ready - Ready to fire weapon
# fire - Weapon is firing

weaponstate = "ready"

# Create keyboard bindings
playWindow.listen()
playWindow.onkeypress(move_left, 'a')
playWindow.onkeypress(move_right, 'd')
playWindow.onkeypress(fire_weapon, 'space')

# Play background music
play_sound('bgm.mp3')

# Main Game Loop
while True:
    playWindow.update()
    move_player()

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
            play_sound('invaderkilled.wav')
            # Reset the weapon
            weapon.hideturtle()
            weaponstate = 'ready'
            weapon.setposition(0, -400)
            # Move enemy off screen when dead
            enemy.setposition(0, 10000)
            # Update the score
            score += 10
            scorestring = 'Score: {}'.format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if isCollision(player, enemy):
            play_sound('explosion.wav')
            # Hide turtles
            player.hideturtle()
            enemy.hideturtle()
            # Print Game Over and break out of game loop
            print('Game Over')
            break

        # Levels
        if len(enemies) == 0:
            level += 1
            enemyspeed *= 1.05

    # Move the player weapon
    if weaponstate == "fire":
        y = weapon.ycor()
        y += weaponspeed
        weapon.sety(y)

    # Make sure bullet disappears when it reaches the top of the screen
    if weapon.ycor() > 275:
        weapon.hideturtle()
        weaponstate = 'ready'
