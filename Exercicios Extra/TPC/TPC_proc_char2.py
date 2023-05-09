'''
Função chamada proc_char2 que permite procurar um caracter num texto
e desenvolver a posição que aparece 1º.
Devolve -1 se não encontrar ou se lhe mandar procurar mais de um caracter ou nenhum.
Esta função permite procurar a partir de uma determinada posição
do texto e permitir ser case sensitive ou não, assim a função terá 4 parâmetros:
- 1º obrigatório: txt - texto
- 2º obrigatório: caract - caracter
- 3º opcional: posi onde começa (por defeito é 0)
- 4º opcional: sensitive (True ou False) por defeito True
'''

def proc_char2(txt, caract, posi=0, sensitive=True):
    i = 0

    if len(caract) != 1:
        return -1

    if sensitive == False:
        txt = txt.lower()
        caract = caract.lower()

    for i in range(posi, len(txt)):
        if txt[i] == caract:
            return i

    return -1
