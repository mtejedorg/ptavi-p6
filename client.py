#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

USAGE = "Usage: python client.py method receiver@IP:SIPport"
SERV_ERROR = "Error: No server listening"

# Cliente UDP simple.

coms = sys.argv

# Cerramos el programa si no nos llaman con el número deseado de argumentos, informando del uso

if len(coms) != 3:
    print USAGE
    sys.exit()

# Inicializamos el programa e interpretamos los comandos
METODO = coms[1].upper()  #Nos pueden pasar el parámetro en minúsculas
servidor = coms[2]
datos = servidor.split("@")
NOMBRE = datos[0]
direccion = datos[1].split(":")
SERVER = direccion[0]
PORT = direccion[1]
if METODO == "BYE" or "INVITE":
    LINE = METODO + " sip:" + NOMBRE + ":" + SERVER + " SIP/2.0\r\n"
else:
    print "Error, método no contemplado"
    print "Métodos contemplados: INVITE, BYE"
    sys.exit()

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    my_socket.connect((SERVER, int(PORT)))
except socket.gaierror: #Cuando la IP es inválida
    print "Error: invalid IP"
    print USAGE
    sys.exit() 
except ValueError:  #Cuando el puerto no es un número
    print "Error: invalid port"
    print USAGE
    sys.exit()

print "Enviando: " + line
my_socket.send(line + '\r\n')

try:
    data = my_socket.recv(1024)
except socket.error:    #Cuando el servidor no existe
    print "Error: No server listening at",
    print SERVER + " port " + PORT
    sys.exit()

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
