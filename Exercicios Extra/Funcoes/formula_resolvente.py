from math import sqrt

def formula_resolvente(a, b, c):
    if a == 0:
        return []
    if b ** 2 - 4 * a * c < 0:
        return[]
    return [(-b + sqrt(b ** 2 - 4 * a * c))/(2*a),(-b-sqrt(b**2 - 4 * a * c))/(2 * a)]
