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
media = 0
cont = 0

for posi in range(30):
    if valores[posi] % 2 == 0:
        total = valores[posi] + total
        cont = cont + 1

media = total / cont

print('A média dos números pares é {}'.format(media))