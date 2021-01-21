from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, position):
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.speed("slowest")

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)



