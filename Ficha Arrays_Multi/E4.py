from os import system
from random import randint
system('cls')

Dimensao = 3
Linhas = 5
Colunas = 4
D = 0
L = 0
C = 0
M = []

# iniciar a matriz com zeros
for D in range(Dimensao):
    M.append([])
    for L in range(Linhas):
        M[D].append([])
        for C in range(Colunas):
            M[D][L].append(randint(-50, 50))

for D in range(1, Dimensao+1):
    print('{}º Dimensão'.format(D))
    for L in range(Linhas):
        for C in range(Colunas):
            print(M[D-1][L])
    print()