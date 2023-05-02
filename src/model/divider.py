from turtle import Turtle


class Divider:
    def __init__(self):
        self.divider = Turtle()
        self.divider.color("dim gray")
        self.divider.pensize(5)
        self.divider.hideturtle()
        self.divider.penup()
        self.divider.goto(0, -300)
        self.divider.setheading(90)
        self.draw_divider()

    def draw_divider(self):
        for i in range(0, 30):
            self.divider.pendown()
            self.divider.forward(10)
            self.divider.penup()
            self.divider.forward(15)

