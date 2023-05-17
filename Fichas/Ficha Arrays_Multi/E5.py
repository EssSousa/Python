# bibliotecas e limpar tela
from random import randint
from pyconio import clrscr, gotoxy

clrscr()
gotoxy(0, 0)

# variaveis
notas = []
media = 0
AL = 0

# dar notas ao aluno
for AL in range(3):
    notas.append(randint(0, 42))
    if notas[AL] > 20 and notas[AL] <= 31:
        notas[AL] -= 11
    else:
        if notas[AL] > 31:
            notas[AL] -= 22
            

print(notas)
