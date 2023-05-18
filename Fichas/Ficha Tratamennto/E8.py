i = 0
txt = ''
letras = "aA"

txt = input('Texto: ')

print('Posições: ', end="")

for i in range(len(txt)):
    if txt[i] in letras:
        print(i, end=" ")
