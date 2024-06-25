import random
import time
from turtle import Screen
from alienshots import Alienshots
from lives import Lives
from shot import Shot
from spaceship import Spaceship
from alien import Alien

# Create screen.
screen = Screen()
screen.title("Breakout")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
# Create Spaceship object for player.
player = Spaceship()

# Lives object representing the lives of the player.
lives = Lives()
# List of aliens
aliens = []
# Object that represents the shots fired by the aliens.
alien_shots = Alienshots()

# Create aliens
for i in range(5):
    alien = Alien(-160 + (i * 80),275)
    aliens.append(alien)


# Player controls
screen.onkeypress(player.shoot, "Up")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


# While there are aliens present or player runs out of lives, game is on.
while len(aliens) > 0 and lives.get() > 0:
    time.sleep(0.1)
    screen.update()

    # If player shot passes the screen limit then remove, else shot keeps moving.
    for shot in player.shots:
        if shot.ycor() > 400:
            player.shots.remove(shot)
        else:
            shot.move()

    # If player shot passes the screen limit then remove, else shot keeps moving.
    for shot in alien_shots.shots:
        if shot.ycor() < -400:
            alien_shots.shots.remove(shot)
        else:
            shot.move()

    # Move aliens.
    for alien in aliens:
        alien.move()

    # If any alien makes contact with a players bullet then remove the alien.
    for alien in aliens:
        for shot in player.shots:
            if alien.distance(shot) < 35:

                alien.hideturtle()

                shot.hideturtle()
                aliens.remove(alien)
                break
    # If any alien bullet makes contact with the player then remove a life and start new round.
    for shot in alien_shots.shots:
        if player.distance(shot) < 15:
            alien_shots.remove_all()
            player.start_position()
            lives.lose_life()
            break

    # Occasionally select a random alien to fire a bullet.
    if random.randint(1, 15) == 1:
        firing_alien = random.choice(aliens)
        alien_shots.add(Shot(firing_alien.xcor(), -1))


# At end of game, remove all bullets from screen and display win/loss message.
player.remove_all()
alien_shots.remove_all()
lives.clear()

if lives.get() == 0:
    lives.goto(0, 0)
    lives.write("You lose!", font=("Arial", 20, "normal"))

else:
    lives.goto(0, 0)
    lives.write("You won!", font=("Arial", 20, "normal"))

screen.update()

screen.exitonclick()

