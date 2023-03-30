# bibliotecas
from random import randint
from pyconio import clrscr, gotoxy

clrscr()
gotoxy(0, 0)

# variaveis
notas = []
media = 0


# dar notas ao aluno
for AL in range(3):
    notas.append(randint(0, 60))
    if notas[AL] > 40:
        notas[AL] = notas[AL] // 2
    if notas[AL] > 20:
        notas[AL] = notas[AL] // 3        

print(notas)