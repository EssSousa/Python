from random import randint


def Array_Sem_Repetidos(QtdPosi, LimiteInf, LimiteSup):
    i = 0
    Array = []
    Num = 0
    Existe = True
    Posi = 0
    if QtdPosi > LimiteSup-LimiteInf+1:
        return []
    for i in range(QtdPosi):
        Existe = True
        while Existe:
            Num = randint(LimiteInf, LimiteSup)
            Posi = 0
            while Posi < len(Array) and Num != Array[Posi]:
                Posi = Posi + 1
            if Posi == len(Array):
                Existe = False
        Array.append(Num)
    return Array