from random import randint

Linhas = 3
Colunas = 7
L = 0
C = 0
M = []

# iniciar a matriz com zeros
for L in range(Linhas):
    M.append([])
    for C in range(Colunas):
        M[L].append(randint(-50, 50))

for L in range(Linhas):
    print(M[L])
