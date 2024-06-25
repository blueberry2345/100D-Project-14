from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.remaining = 3
        self.color("green")
        self.penup()
        self.update()

    def get(self):
        return self.remaining

    def update(self):
        self.clear()
        self.goto(-20, -50)
        self.write(self.remaining, font=("Arial", 20, "normal"))

    def lose_life(self):
        self.remaining -= 1
        self.update()