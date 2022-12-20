from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
   """A FUNÇÃO MOVE_SPEED AUMENTA A VELOCIDADE DA BOLA QUANDO ELA ACERTA A PÁ"""

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
"""TODAS A VEZ Q A BOLA SE MEXER VAI ACRESCENTAR 3 PIXELS NA COORDENADA"""
    def bounce_y(self):
        self.y_move *= -1
"""MULTIPLICANDO POR -1 SE INVERTE A DIREÇÃO DA BOLA"""

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
