from turtle import Turtle

class Shot(Turtle):

    def __init__(self, x_location, direction):
        super().__init__()
        self.direction = direction
        self.shots = []
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.1)
        self.color("white")
        self.penup()
        self.goto(x_location, -220 * direction)

    def move(self):
        self.goto(self.xcor(), self.ycor() + 10 * self.direction)