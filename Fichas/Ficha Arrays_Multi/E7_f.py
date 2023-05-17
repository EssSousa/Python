from os import system
from random import randint
system('cls')

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
verificar = 0

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
    media_disc_AL.append([])
    for disc in range(3):
        tot = 0
        verificar = 0
        for exame in range(3):
            if notas_disc_AL[AL][disc][exame] <= 9:
                verificar = 1
            tot += notas_disc_AL[AL][disc][exame]
        if verificar == 1:
            media = -1
        else:
            media = tot // 3
        media_disc_AL[AL].append(media)


for AL in range(6):
    print('Nome do aluno(a): {}'.format(nome_alunos[AL]))
    for disc in range(3):
        print('{}:'.format(nome_disc[disc][0:3]), end=" ")
        if media_disc_AL[AL][disc] == -1:
            print('---', end=" ")
        else:
            print('{}'.format(media_disc_AL[AL][disc]), end="")
        print()
    print()

print()
print('Alunos que têm a disciplina de Programação por fazer: ')

for AL in range(6):
    for disc in range(3):
        if media_disc_AL[AL][disc] == -1:
            print(' - {}'.format(nome_alunos[AL]))