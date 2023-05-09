'''
Criar um programa que permita ler um texto com um minimo de 3 caracteres
e um máximo de 10, e que posteriormente imprima linha a linha:

- a) cada um dos caracteres do texto, ou seja escreva o texto na vertical
- b) os caracteres do texto por ordem inversa, ou seja, no final o texto pode ser lido debaixo para cima 
'''

# variaveis
txt = ""
i = 0

# ler a variavel
txt = str(input('Introduza o texto: '))

while len(txt) < 3 or len(txt) > 10:
    print('Numero de caracteres incorreto')
    txt = str(input('Introduza o texto: '))

# imprimir
for i in range(i, len(txt)):
    print(txt[i])
