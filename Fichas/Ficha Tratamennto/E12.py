i = 0
txt = ''

txt = input('Texto: ')
while len(txt) < 3 or len(txt) > 10:
    print('Numero incorreto de caracteres')
    txt = input('Texto: ')



for i in range(len(txt)):
    print(txt[i],end="")
    if i != len(txt)-1:
        print('|',end="")

