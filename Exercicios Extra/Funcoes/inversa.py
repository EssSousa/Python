def inversa(orig):
    tamanho = len(orig)
    inv = [0] * tamanho
    x = 0
    for x in range(tamanho):
        inv[x] = orig[tamanho - x]