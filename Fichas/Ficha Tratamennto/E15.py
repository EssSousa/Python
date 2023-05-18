posi = 0
txt = ''
txt2 = ''
txt3 = ''
letra = ''

txt = input('Texto 1: ')

txt2 = input('Texto 2: ')

while posi < len(txt) and posi < len(txt2):
    txt3 = txt3 + txt[posi] + txt2[posi]
    posi += 1

if posi < len(txt):
    txt3 += txt[posi::]
else:
    if posi < len(txt2):
        txt3 += txt2[posi::]
    

print('Texto final: {}'.format(txt3))
