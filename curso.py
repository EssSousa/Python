from time import sleep
from pyconio import *
import sys

# variaveis
i = 0
texto = 'Curso Técnico de Gestão e Programação de Sistemas Informáticos'
resposta = 'Aluno'
passw = '********'
# funcao

def trabalhar():
    while True:
        sleep(0.5)
        clrscr()
        gotoxy(0,0)
        textcolor(Red)
        print('Escola Secundária Santa Maria Maior')   
        gotoxy(0, 4)
        textcolor(Green)
        for i in range(len(texto)):
            sys.stdout.write(texto[i])
            sys.stdout.flush()
            sleep(0.1)

        sleep(0.5)
        gotoxy(0, 5)
        print()
        print('\tUsuário: ')
        print('\t > ', end="")
        for i in range(len(resposta)):
            sys.stdout.write(resposta[i])
            sys.stdout.flush()
            sleep(0.1)
        print()
        sleep(1)
        print()
        print('\tPassword: ')
        print('\t > ', end="")
        for i in range(len(passw)):
            sys.stdout.write(passw[i])
            sys.stdout.flush()
            sleep(0.1)
        sleep(1)
        print()
        textcolor(Blue)
        textbackground(White)
        print(' *Acesso Concedido!* ')
        textbackground(Black)
        sleep(2)
trabalhar()
