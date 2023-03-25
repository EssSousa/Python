from random import randint

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
        M.append([])
        for C in range(Colunas):
            M[L].append(randint(-50, 50))

for L in range(Linhas):
    print(M[L])
