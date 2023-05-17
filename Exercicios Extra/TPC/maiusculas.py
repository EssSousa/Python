'''
Cria um programa em python que permita ler um texto
que pode ter caracteres maiusculos e minusculos
e que posteriormente imprima esse texto sem os caracteres minusculos
'''

# variaveis
txt = ''
txtFinal = ''
f = 0

txt = input('texto: ')

for f in range(0, len(txt)):
    if txt[f]:
        txtFinal += txt[f]

print(txtFinal)
