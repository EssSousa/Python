from random import randint

valores = [500] * 30
posi = 0
p = 0
r = 0

while posi <= 29:
    r = randint(-100, 100)
    p = 0
    while p < posi and valores[p] != r:
        p = p + 1
    if p == posi:
            valores[posi] = r
            posi = posi + 1

# -------------------------------------------
maior = -500
Nposi = 0
posi = 0

for posi in range(1, 30, 2):
    if abs(valores[posi]) > maior:
        maior = abs(valores[posi])
        Nposi = posi
    print(Nposi)
