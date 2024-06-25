from turtle import Turtle
from shot import Shot

class Spaceship(Turtle):

    def __init__(self):
        super().__init__()
        self.shots = []
        self.shape("circle")
        self.color("white")
        self.penup()
        self.start_position()

    def move_left(self):
        if self.xcor() > -390:
            self.goto(self.xcor() - 10, self.ycor())

    def move_right(self):
        if self.xcor() < 390:
            self.goto(self.xcor() + 10, self.ycor())

    def shoot(self):
        new_shot = Shot(self.xcor(), 1)
        self.shots.append(new_shot)

    def start_position(self):
        self.goto(0, -250)

    def remove_all(self):
        for shot in self.shots:
            shot.goto(shot.xcor(), 500)


