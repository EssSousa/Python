from pyconio import *
from os import get_terminal_size

def menu(options):
    maior = 0
    validos = "01234"
    frase = "Qual sua opcao: "
    clrscr()

    # obter maior texto
    for i in range(len(options)):
        if len(options[i]) > maior:
            maior = len(options[i])

    maior = maior + 4

    # calcular a posição do x para as opções
    posiX = get_terminal_size().columns / 2- maior / 2

    # ciclo para imprimir as opções
    for f in range(len(options)):
        gotoxy(posiX, 5 + f)
        print(f, "-", options[f])
        validos += str(f)

    # imprimir texto para pedir opção
    gotoxy(get_terminal_size().columns/2 - len(frase)/2 + 2, 7 + f)
    print(frase)

    # pedir opção
    op = "-"
    while op not in validos:
        gotoxy(get_terminal_size().columns / 2 + len(frase)/2 + 2, 7+f)
        op = getch()
    print(op)
    return int(op)

opcoes=['Sair','Nível 1','Nível 2','Nível 3','Nível 4']
menu(opcoes)