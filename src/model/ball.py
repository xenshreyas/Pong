from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x = 10
        self.y = 10
        self.color = "white"
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05
