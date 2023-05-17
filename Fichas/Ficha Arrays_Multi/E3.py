from os import system
from random import randint
system('cls')

A = 0
B = 0
C = 0
M = []

# iniciar a matriz com zeros
for A in range(5):
    M.append([])
    for B in range(4):
        M[A].append([])
        for C in range(3):
            M[A][B].append(randint(10, 99))
