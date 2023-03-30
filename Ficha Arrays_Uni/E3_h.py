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

maior = 200
menor = 200
posimaior = 0
posimenor = 0

for posi in range(30):
    if maior < valores[posi]:
        maior = valores[posi]
        posimaior = posi
    if menor > valores[posi]:
        posimenor = posi

print('{} - {}, {} - {}'.format(posimaior, maior, posimenor, menor))
