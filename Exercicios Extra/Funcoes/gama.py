def gama(inicial = 0, final = 1, step = 1):
    if step == 0:
        return
    if step > 0:
        if inicial <= final:
            print(inicial)
            gama(inicial+step, final, step)
    else:
        if inicial >= final:
            print(inicial)
            gama(inicial+step, final, step)

