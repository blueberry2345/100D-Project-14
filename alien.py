import time
from turtle import Turtle

class Alien(Turtle):

    def __init__(self, x_location, y_location):
        super().__init__()
        self.start_location = x_location
        self.time_last_movement = time.time()
        self.x_direction = 1
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(x_location, y_location)



    def move(self):
        if (time.time() - self.time_last_movement) > 1:
            if self.xcor() >= (self.start_location + 10) or self.xcor() <= (self.start_location - 10):
                self.x_direction *= -1
            self.goto(self.xcor() + (10 * self.x_direction), self.ycor())
            self.time_last_movement = time.time()