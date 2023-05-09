'''
Esta função procura um subtexto dentro de um outro texto,
Começando na posição POSI do texto, que por defeito é o inicio.
Contudo, se encontrar o subtexto, a sua posição é indicada tendo
por base todo o texto e não a posição de inicio da procura.
Esta função permite "desativar" o Case Sensitive. Se o ultimo
parametro for FALSE, então um "a" passa a ser igual a um "A", por exemplo.
Caso o subtexto não exista é devolvido -1.
Caso contrário, devolve a posição do primeiro caracter
do subtexto no texto. Exemplo: Procura "ri" em "Maria", devolve 2.
Relembrar que o primeiro caracter do texto está na posição ZERO.
'''

def proc_subtext(txt, subtext, posi=0, sensitive=True):
    txtsub = ''

    if sensitive == False:
        txt = txt.lower()
        subtext = subtext.lower()

    for i in range(posi, len(txt)):
        if txt[i] == subtext[i]:
            txtsub = txt[i]
        else:
            txtsub = ''
        if txtsub == subtext:
            return i-len(txtsub)

    return -1


proc_subtext("Maria","ri",0, False)