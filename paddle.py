from turtle import Turtle

'''REPARAR COMO SEPAROU CADA PARTE DO JOGO EM UM MÓDULO E SÓ IMPORTOU DE UM PARA OUTRO.
APLICANDO AQUI O CONCEITO DE HERANÇA'''
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    '''só vai mexer na posição y(altura), somando 20 pixels ao atual, '''

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

'''A CLASSE PADDLE PASSA A CLASSE TURTLE (QUE É UMA CLASSE PRÉ CRIADA) COMO ARGUMENTO,
E DEPOIS HERDA TODAS AS FUNÇÕES ATRAVÉS DO COMANDO super().__init__().
DURANTE A FEITURA DO CÓDIGO USOU O COMANDO REPLACE PARA SUBSTITUIR VÁRIAS PALAVRAS IGUAIS POR OUTRAS,
NESSE CASO, PADDLE POR SELF. REPARAR QUE O ARGUMENTO POSITION VALIDA OS ARGUMENTOS
DE POSIÇÃO PASSADOS NA CLASSE PADDLE, DENTRO DO MAIN'''
