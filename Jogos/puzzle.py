from pyconio import *
from random import *

# -------------------------- variaveis ------------------------------
solucao = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
a = 0
b = 0
col = 3
lin = 3
jogo = []
saco = "012345678"
espaco = []
mov = 0
game = 1

# ---------------------------- teclas --------------------------------
teclas = "wasdWASDfF"
cima = 'wW'
baixo = 'sS'
esq = 'aA'
dire = 'dD'
sair = "fF"

# --------------------- função do tabuleiro --------------------------
def imprimir_tabuleiro(array, x, y):
    for i in range(len(array)):
        gotoxy(x, y+i)
        for k in range(len(array[i])):
            if array[i][k] == 0:
                print(" 0", end="")
            else:
                print("", array[i][k], end="")


# --------------------- iniciar o array ------------------------------
for a in range(col):
    jogo.append([])
    for b in range(lin):
        posi = randint(0, len(saco) - 1)
        letra = saco[posi]
        if letra == "0":
            espaco_x = a
            espaco_y = b
        saco = saco.replace(letra, "")
        jogo[a].append(int(letra))


# ---------------------- INICIAR O JOGO ------------------------------
clrscr()
gotoxy(11, 5)
textcolor(Yellow)
print("SOLUCAO")
textcolor(White)
imprimir_tabuleiro(solucao, 11, 7)

gotoxy(21, 5)
textcolor(Yellow)
print("JOGO")
textcolor(White)
imprimir_tabuleiro(jogo, 21, 7)

gotoxy(40, 5)
textcolor(Yellow)
print('Lista de comandos: ')
gotoxy(40, 7)
textcolor(Green)
print('Movimento para cima - ',end="")
textcolor(Blue)
print('W')
gotoxy(40, 9)
textcolor(Green)
print('Movimento para Baixo - ',end="")
textcolor(Blue)
print('S')
gotoxy(40, 11)
textcolor(Green)
print('Movimento para Esquerda - ',end="")
textcolor(Blue)
print('A')
gotoxy(40, 13)
textcolor(Green)
print('Movimento para Direita - ',end="")
textcolor(Blue)
print('D')
gotoxy(40, 15)
textcolor(Red)
print('Movimento para cima - F',end="")
textcolor(White)

gotoxy(30,30)
# ------------------------- JOGO COM TECLAS --------------------------

while game == 1 or jogo != solucao: 
    tecla = "€"
    while tecla not in teclas:
        tecla = getch()
        if tecla in cima:
            if espaco_x < 2:
                jogo[espaco_x][espaco_y] = jogo[espaco_x + 1][espaco_y]
                espaco_x += 1
                jogo[espaco_x][espaco_y] = 0
                imprimir_tabuleiro(jogo, 21, 7)
                mov += 1
                gotoxy(10,15)
                print('Movimentos: {}'.format(mov))
                gotoxy(10, 17)
                print('PARAAAAA CIIMMAAAAAAAAAAAAAA!!!!!!')
        else:
            if tecla in baixo:
                if espaco_x > 0:
                    jogo[espaco_x][espaco_y] = jogo[espaco_x - 1][espaco_y]
                    espaco_x -= 1
                    jogo[espaco_x][espaco_y] = 0
                    mov += 1
                    gotoxy(10, 15)
                    print('Movimentos: {}'.format(mov))
                    imprimir_tabuleiro(jogo, 21, 7)
                    gotoxy(10, 17)
                    print('PARAAAAA BAAAIIIIXXOOOUUUU!!!!!!')
            else:
                if tecla in dire:
                     if espaco_y > 0:
                        jogo[espaco_x][espaco_y] = jogo[espaco_x][espaco_y - 1]
                        espaco_y -= 1
                        jogo[espaco_x][espaco_y] = 0
                        mov += 1
                        gotoxy(10,15)
                        print('Movimentos: {}'.format(mov))
                        imprimir_tabuleiro(jogo, 21, 7)
                else:
                    if tecla in esq:
                        if espaco_y < 2:  
                            jogo[espaco_x][espaco_y] = jogo[espaco_x][espaco_y + 1]
                            espaco_y += 1
                            jogo[espaco_x][espaco_y] = 0
                            mov += 1
                            gotoxy(10,15)
                            print('Movimentos: {}'.format(mov))
                            imprimir_tabuleiro(jogo, 21, 7)
                    else:
                        if tecla in sair:
                            gotoxy(10, 19)
                            if jogo != solucao:
                                print('Encerrado mas não concluido! Com {} movimentos'.format(mov))
                            game = 0

if jogo == solucao:
    gotoxy(10, 19)
    print('Parabéns! Concluido com {}'.format(mov))


