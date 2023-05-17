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
for posi in range(1, len(valores) -1):
    if valores[posi-1] < valores[posi] and valores[posi+1] < valores[posi]:
        print('Posição: {} - Nº: {}'.format(posi, valores[posi]))
