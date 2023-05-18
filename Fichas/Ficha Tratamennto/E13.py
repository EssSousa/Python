i = 0
txt = ''
txtFinal = ''

txt = input('Texto: ')
while len(txt) < 10 or len(txt) > 30:
    print('Numero incorreto de caracteres')
    txt = input('Texto: ')

for i in range(len(txt)):
    if txt[i] != " ":
        txtFinal += txt[i]
    else:
        txtFinal += "|"

print(txtFinal)
