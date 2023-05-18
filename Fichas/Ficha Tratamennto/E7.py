i = 0
txt = ''

txt = input('Texto:')

print('Posições: ', end="")

for i in range(len(txt)):
    if txt[i] == "a":
        print(i, end=" ")
