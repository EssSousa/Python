from random import randint
from pyconio import *
from os import get_terminal_size

computador = 0
usuario = 0


def jogo(nivel):
    pass

def menu(options):
    maior = 0
    validos = "01234"
    frase = "Qual sua opcao: "
    clrscr()

    for i in range(len(options)):
        if len(options[i]) > maior:
            maior = len(options[i])

    posiX = get_terminal_size().columns/2-(maior + 4)/2

    for f in range(len(options)):
        gotoxy(posiX, 5 + f)
        print(f, "-", options[f])
        validos += str(f)

    gotoxy(get_terminal_size().columns/2 - len(frase)/2 + 2, 7 + f)
    print(frase)
    gotoxy(get_terminal_size().columns / 2 + len(frase)/2 + 2, 7+f)
    op = "-"
    while op not in validos:
        op = getch()
        if op == '1':
            jogo(1)
        else:
            if op == '2':
                jogo(2)
            else:
                if op == '3':
                    jogo(3)
                else:
                    return

opcoes=['Sair','Nível 1','Nível 2','Nível 3']

# --------------------- programa principal -------------------
menu(opcoes)