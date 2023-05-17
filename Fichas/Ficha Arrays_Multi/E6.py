from pyconio import *
from random import randint
from os import system
system('cls')

a = 0
b = 0
c = 0

aluno = ['Ana', 'Carlos', 'Helena', 'Iídio', 'Joana', 'Luís']
notas = []

for a in range(6):
    notas.append([])
    for b in range(3):
        notas[a].append([])
        N = randint(0, 31)
        if N > 20:
            N = N - 11
        notas[a][b].append(N)

for a in range(6):
    textcolor(Blue)
    print('Aluno: ', end="")
    textcolor(White)
    print('{}'.format(aluno[a]))
    for b in range(3):
        textcolor(Red)
        print('{}º teste: '.format(b+1), end="")
        textcolor(White)
        print(notas[a][b])
    print()
    print()
