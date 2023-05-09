L = 0
C = 0
Matriz = []
for L in range(1, 5):
    Matriz.append([])
    for C in range(1,4):
        Matriz[L-1].append(L * 10 + C)

print(Matriz)
