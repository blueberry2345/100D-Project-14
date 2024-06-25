class Alienshots():

    def __init__(self):
        self.shots = []

    def add(self, shot):
        self.shots.append(shot)

    def remove(self, shot):
        shot.hideturtle()
        self.shots.remove(shot)

    def remove_all(self):
        for shot in self.shots:
            shot.goto(shot.xcor(), -500)