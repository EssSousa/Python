i = 0
txt = ''
txt2 = ''
txtFinal = ''

txt = input('Texto: ')
while len(txt) < 10 or len(txt) > 30:
    print('Numero incorreto de caracteres')
    txt = input('Texto: ')

txt2 = input('Texto 2: ')
while len(txt2) < 10 or len(txt2) > 30:
    print('Numero incorreto de caracteres')
    txt2 = input('Texto: ')

print(txt+txt2)