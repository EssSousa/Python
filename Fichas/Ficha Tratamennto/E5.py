# variaveis
texto = ''
caract = 0
i = 0

# ler o texto
texto = str(input('Digite o texto desejado: '))

# saber quantos espaços tem
for i in range(0, len(texto)):
    if texto[i] != " ":
        caract += 1    

# imprimir 
print('A string: {} \n Possui {} espaços!'.format(texto, caract))
