'''
Criar um programa em pyhton que permita ler um texto e posteriormente imprimir:
a) Imprimir numa linha este texto com os caracteres todos em maisculas
b) Imprimir numa linha este texto com os caracteres todos em minusculas
c) Imprimir a quantidade de espaços que existem no texto lido
d) Imprimir o numero de caracteres do texto lido mas sem contar com os espaços
'''

# variaveis
texto = ''

# interface grafica
print('--------------------------------')
print('Este programa permite imprimir: ')
print('- O texto em maisuculas')
print('--------------------------------')

# ler o texto
texto = str(input('Digite o texto desejado: '))

# imprimir 
print('Texto em maisculas: {}'.format(texto.upper()))
