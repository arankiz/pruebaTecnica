# -*- coding: cp1252 -*-
import time
import datetime
import socket
import sys

i=0
#---------------------------------------------------
try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")
#---------------------------------------------------

def ejecutaScript():
    #python myscript.py
    for i in range(10):
        x = datetime.datetime.now()
        shell.write("Equipo_A: Fecha y hora = %s" % x,"KEYWORD")
        time.sleep(1)
        print("---- ")
    print()
    #---------------------------------------------------
    # Creando un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta el socket en el puerto cuando el servidor esté escuchando
    server_address = ('localhost', 10018)
    sock.connect(server_address)
    try:
        # Enviando datos
        message = "%s" %x
        print >>sys.stderr, 'enviando de Equipo_A:  "%s"' % message
        sock.sendall(message)
        # Buscando respuesta
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(19)
            amount_received += len(data)
            #print >>sys.stderr, 'recibiendo "%s"' % data
            shell.write("recibiendo de Equipo_B: %s" % data,"DEFINITION")
    finally:
        print >>sys.stderr, '----'
        #sock.close()
while True:
    ejecutaScript()
