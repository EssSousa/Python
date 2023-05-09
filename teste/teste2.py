import socket
from pyconio import clrscr, gotoxy
from time import sleep

clrscr()
gotoxy(0, 0)

'''
If [0] - Has Connection
Else - Doesn't Has connection

# restos de codigo

resposta = client.recv(1024)
print(resposta.decode())

connection = client.connect_ex(("bancocn.com", port))
'''

option = 0
port = 0
ports = [21, 22, 80, 443, 445, 3306, 25]
open_ports = []
close_ports = []
ip = 0
work = 1

host = str(input('Host: '))
sleep(0.5)
print('\nPreparing...')
sleep(0.5)

try: 
    ip = socket.gethostbyname(host)

    # searching for open ports
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        connection = client.connect_ex((host, port))

        if connection == 0:
            open_ports.append(port)
        else:
            close_ports.append(port)

except:
    print('Invalid URL or IP Adress')
    work = 0

# if have open ports show the list else don't show nothing
clrscr()
gotoxy(0, 0)

print('-------------------', len(host)*"-", sep="")
print('--- Host selected:', host)
if ip != 0:
    print('--- IP:', ip)
else: 
    print('--- IP: INVALID HOST')
print('\n--- Has connection?\n')
if work == 0:
    print('No')
else: 
    print('Yes')

print('-------------------', len(host)*"-", sep="")

if open_ports != []:
    print("Open Ports:", open_ports)
    if close_ports != []:
        print('-------------------', len(host)*"-", sep="")
        print("Close Ports:", close_ports)
else:
    print('None Open ports')
print('-------------------', len(host)*"-", sep="")
