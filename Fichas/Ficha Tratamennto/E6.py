txt = ''
txtFinal = ''
i = 0

txt = input('Texto: ')

for i in range(len(txt)):
    if txt[i].isupper():
        txtFinal += txt[i]

print(txtFinal)