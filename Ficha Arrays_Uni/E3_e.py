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

total = 0

for posi in range(0, 30):
    if valores[posi] <= 10 and valores[posi] >= -10:
        total = total + 1

print('Existem {} números entre -10 e 10')