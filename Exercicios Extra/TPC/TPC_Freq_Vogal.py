'''
Frequencia absoluta das vogais
são x a's
sao x e's
sao x i's
'''
# variaveis
text = "Estamos todos a perceber isto!?"
posi = 0
a = 0
e = 0
i = 0
o = 0
u = 0
outro = 0

# verificar
while posi < len(text):
    if text[posi] == "a" or text[posi] == "A":
        a+=1
    elif text[posi] == "e" or text[posi] == "E":
        e+=1
    elif text[posi] == "i" or text[posi] == "I":
        i+=1
    elif text[posi] == "o" or text[posi] == "O":
        o+=1
    elif text[posi] == "u" or text[posi] == "U":
        u+=1
    else:
        outro += 1
    posi+=1

print('String: ',text)
print('A: ',a)
print('E: ',e)
print('I: ',i)
print('O: ',o)
print('U: ',u)
print('Outros: ',outro)
