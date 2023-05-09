from os import system
from random import randint
system('cls')

A = 0
B = 0
C = 0
M = []
cont = 0

# iniciar a matriz com zeros
for A in range(5):
    M.append([])
    for B in range(4):
        M[A].append([])
        for C in range(3):
            M[A][B].append(randint(10, 99))

for C in range(5):
    for B in range(4):
        cont = 0
        for A in range(3):
            if cont < 2:
                print(M[A][B][C], end=" - ")
            else: 
                print(M[A][B][C])
            cont += 1
        print()
    Cant = C

    print()
