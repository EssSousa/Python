from math import sqrt

def f(x):
    if x == 0:
        return 25
    else:
        if x > 0:
            return x * sqrt
        else:
            return 'ERRO! Número INVÁLIDO!'
        