'''
Cria um programa em python que permita ler 2 textos cada um deles
com um minimo de 3 caracteres e um maximo de 10 e que posteriormente
crie e imprima um terceiro texto que:
- a) junte o 1º e 2º texto
- b) junte os caracteres das posições impares do 1º texto e aos caracteres pares do 2º, usando o fatiamento
- c) junte os caracteres das 2 primeiras posições do 1º textp com o 2º texto e com as 2 ultimas posições do 
primeiro texto (por esta ordem)
- d) junte alternadamente os caracteres de cara um dos textos, começando pelo 1º texto como os textos podem
ser de tamanhos diferentes no final juntar os restantes caracteres que sobrarem no fim 
'''

# variaveis
txt1 = ''
txt2 = ''
txt3 = ''
i = 0

# ler o texto
txt1 = str(input('Introduza o 1º texto: '))

while len(txt1) < 3 or len(txt1) > 10:
    print('Numero incorreto de caracteres')
    txt1 = str(input('Introduza o texto: '))

txt2 = str(input('Introduza o 2º texto: '))

while len(txt2) < 3 or len(txt2) > 10:
    print('Numero incorreto de caracteres')
    txt2 = str(input('Introduza o texto: '))
    
# -------------------------------------------------------
# a)
# juntar o 1º e o 2º texto
print(txt1 + txt2)
print('\n----------------------------\n')


# -------------------------------------------------------
# b)
# juntar os caracteres impares do 1º com os pares do 2º


print(txt3)
print('\n----------------------------\n')


# -------------------------------------------------------
# c)
# juntar os 2 primeiros caracteres do 1º com os 2 ultimos do 2º
while txt1_extra != "" and txt2_extra != "":
    pass