from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

''''CÓDIGO DE CRIAÇÃO DA TELA'''

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
'''CÓDIGO DE CRIAÇÃO DA PÁ (PADDLE)'''
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
'''LEMBRAR SEMPRE, QUANDO SE PASSA UMA FUNÇÃO COMO PARÂMETRO, NÃO SE USA OS PARÊNTESES ().
 AQUI AS PÁS DE CADA LADO SÃO CONTROLADAS POR TECLAS DIFERENTES.'''
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
'''ELA JÁ CRIOU O MÉTODO NO PRINCIPAL (main) ANTES MESMO DE EXPLICÁ-LO NO MÓDULO BALL'''

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
"""ELA CRIOU DOIS BOUNCES (QUE SIGNIFICA VOLTAR) UM PARA Y E OUTRO PARA X, A LÓGICA É QUE A BOLA
VAI ENCOSTAR NA PAREDE E NO CÓDIGO DE BAIXO O SISTEMA VAI VERIFICAR A DISTÂNCIA PARA A PAREDE E
PARA O PÁ"""

screen.exitonclick()