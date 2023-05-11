'''
Cria um programa em python que permita ler um texto
que pode ter caracteres maiusculos e minusculos
e que posteriormente imprima esse texto sem os caracteres minusculos
'''

# variaveis
txt = ''
txtMaius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
txtFinal = ''

txt = input('texto: ')

for i in range(0, len(txt)):
    if txt[i] in txtMaius:
        txtFinal += txt[i]

print(txtFinal)
