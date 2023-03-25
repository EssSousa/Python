def media(*numeros):
    total = 0
    n = 0
    for n in numeros: 
        total = total + n
    return total / len(numeros)