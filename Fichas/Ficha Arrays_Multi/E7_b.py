from os import system
from random import randint
from pyconio import * 
system('cls')
'''
Exemplos:

         PSI  M     PORT  M     MAT  M
Ana    15,12,10   12,10,8    14,12,10

Carlos 18,16,14   17,15,13   16,16,13

...

...

Alinhar os nomes pela ultima letra
'''

# -------------- variaveis --------------------
disc = 0
AL = 0
nome_disc = ["PSI", "PORT", "MAT"]
notas_disc_AL = []
nome_alunos = ["Ana", "Carlos", "Helena", "Ilídio", "Joana", "Luís"]
media_disc_AL = []
media = 0
exame = 0
tot = 0

# ---------------------------------------------

for AL in range(6):
    notas_disc_AL.append([])
    for disc in range(3):
        notas_disc_AL[AL].append([])
        for notas in range(3):
            N = randint(0, 31)
            if N > 20:
                N = N - 11
            notas_disc_AL[AL][disc].append(N)


for AL in range(6):
    textcolor(Red)
    print('Nome do Aluno: ', end="")
    textcolor(White)
    print('{}'.format(nome_alunos[AL]))
    textcolor(Yellow)
    print('Nota de Português: ')
    for disc in range(3):
        textcolor(Blue)
        print('{}º teste: '.format(disc+1), end="")
        textcolor(White)
        print('{}'.format(notas_disc_AL[AL][2][disc]))
    print()
    print()
