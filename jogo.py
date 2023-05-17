import turtle

# Configuração da janela do jogo
janela = turtle.Screen()
janela.title("Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Raquete 1
raquete1 = turtle.Turtle()
raquete1.speed(0)
raquete1.shape("square")
raquete1.color("white")
raquete1.shapesize(stretch_wid=6, stretch_len=1)
raquete1.penup()
raquete1.goto(-350, 0)

# Raquete 2
raquete2 = turtle.Turtle()
raquete2.speed(0)
raquete2.shape("square")
raquete2.color("white")
raquete2.shapesize(stretch_wid=6, stretch_len=1)
raquete2.penup()
raquete2.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(40)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# Funções de movimento das raquetes
def raquete1_para_cima():
    y = raquete1.ycor()
    if y < 250:
        y += 20
    raquete1.sety(y)

def raquete1_para_baixo():
    y = raquete1.ycor()
    if y > -240:
        y -= 20
    raquete1.sety(y)

def raquete2_para_cima():
    y = raquete2.ycor()
    if y < 250:
        y += 20
    raquete2.sety(y)

def raquete2_para_baixo():
    y = raquete2.ycor()
    if y > -240:
        y -= 20
    raquete2.sety(y)

# Vinculação dos controles das raquetes
janela.listen()
janela.onkeypress(raquete1_para_cima, "w")
janela.onkeypress(raquete1_para_baixo, "s")
janela.onkeypress(raquete2_para_cima, "Up")
janela.onkeypress(raquete2_para_baixo, "Down")

# Loop principal do jogo
while True:
    janela.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Verificação das colisões
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete2.ycor() + 50 and bola.ycor() > raquete2.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete1.ycor() + 50 and bola.ycor() > raquete1.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1