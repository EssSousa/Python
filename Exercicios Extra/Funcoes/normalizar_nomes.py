'''
Pode usar:
- Find
- Upper
- Lower
'''
nome = "   sOUsA  "

def norm_nome_proprio(nome):
    # apagar os espaços no inicio
    while nome[0] == " ":
        nome = nome[1:] 

    # apagar os espaços no fim
    while nome[-1] == " ":
        nome = nome[0:len(nome)-1]

    


    return nome


print(norm_nome_proprio(nome))

