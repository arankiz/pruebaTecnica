# -*- coding: cp1252 -*-
import time
import datetime
import socket
import sys

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlace de socket y puerto
server_address = ('localhost', 10018)
sock.bind(server_address)
sock.listen(1)

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
        shell.write("Equipo_B: Fecha y hora = %s" % x,"DEFINITION")
        time.sleep(1)
        print("---- ")
    print() 
    #---------------------------------------------------
while True:
    ejecutaScript()
    # Esperando conexion
    connection, client_address = sock.accept()
    print >>sys.stderr, 'concexion desde', client_address
    # Recibe los datos en trozos y reetransmite
    data = connection.recv(19)
    #print >>sys.stderr, 'recibido "%s"' % data
    shell.write("recibido de Equipo_A: %s" % data,"KEYWORD")
    if data:
        x = datetime.datetime.now()
        message = "%s" %x
        print >>sys.stderr, '----'
        print >>sys.stderr, 'enviando de Equipo_B: "%s"' % message
        connection.sendall(message)
        #connection.sendall(data)
    else:
        print >>sys.stderr, 'no hay mas datos', client_address
        break
    # Cerrando conexion
    #connection.close()
    #print >>sys.stderr, 'no hay mas datos', client_address
