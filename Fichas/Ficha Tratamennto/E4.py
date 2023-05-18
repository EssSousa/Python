# variaveis
texto = ''
esp = 0
i = 0

# interface grafica
print('--------------------------------')
print('Este programa permite imprimir: ')
print('- A quantidade de espaços')
print('--------------------------------')

# ler o texto
texto = str(input('Digite o texto desejado: '))

# saber quantos espaços tem
for i in range(0, len(texto)):
    if texto[i] == " ":
        esp += 1    

# imprimir 
print('A string: {} \n Possui {} espaços!'.format(texto, esp))
