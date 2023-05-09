'''
Exemplos:

         PSI  M     PORT  M     MAT  M
Ana    15,12,10   12,10,8    14,12,10

Carlos 18,16,14   17,15,13   16,16,13

...

...

Alinhar os nomes pela ultima letra
'''

from random import randint

# -------------- variaveis --------------------
nome = ""
disc = 0
AL = 0
nome_disc = ["PSI", "PORT", "MAT"]
notas_disc_AL = []
nome_alunos = ["Ana", "Carlos", "Helena", "Ilídio", "Joana", "Luís"]
media_disc_AL = []

# ---------------------------------------------

for AL in range(6):
    media_disc_AL.append([])
    for disc in range(3):
        media_disc_AL[AL].append(randint(0, 20))

for AL in range(6):
    notas_disc_AL.append([])
    for disc in range(3):
        notas_disc_AL[AL].append([])
        for notas in range(3):
            N = randint(0, 31)
            if N > 20:
                N = N - 11
            notas_disc_AL[AL][disc].append(N)

print(nome_disc)
print(nome_alunos)
print(notas_disc_AL)
