'''
Crie um programa que permita ler um texto com o minimo de 10 caracteres
e um máximo de 30 caracteres e que posteriormente imprima:
- a) o texto de tras para a frente, usando as regras do fatiamento
- b) o texto de tras para a frente, sem usar as regras do fatiamento
- c) os caracteres que se encontram nas posições pares, sem usar as regras do fatiamento
- d) os caracteres que se encontram em posições impares, usando as regras do fatiamento
- e) os caracteres que se encontram nas posições multiplas de 5, sem usar as regras do fatiamento
- f) os caracteres que se encontram nas posições divisiveis por 3, usando as regras do fatiamento
'''

# variaveis 
texto = ""
i = 0

# ler o texto
texto = str(input('Digite o texto: '))

while len(texto) < 10 or len(texto) > 30:
    print('numero incorreto de caracteres')
    texto = str(input('Digite o texto: '))
print()

# a)
# imprimir a usar as regras do fatiamento
print('a) ------------------------------')
print(texto[::-1])

print()

# b)
# imprimir sem usar as regras
print('b) ------------------------------')
for i in range(len(texto)-1,-1,-1):
    print(texto[i],end="")
print()

# c)
# imprimir os caracteres pares
for i in range(0, len(texto), 2):
    print(texto[i],end="")

print()

# d)
# imprimir os caracteres impares
print(texto[1:len(texto):2])

# e)
# imprimir os caracteres em posições multiplas de 5
for i in range(0, len(texto), 5):
    print(texto[i],end="")

print()

# f)
# imprimir os caracteres em posições multiplas de 5
print(texto[0:len(texto):3])
