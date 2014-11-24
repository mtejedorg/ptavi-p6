#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys


class SIPHandler(SocketServer.DatagramRequestHandler):
    """
    SIP server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        line = self.rfile.read()
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            print "El cliente nos manda " + line

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":

    USAGE = "Usage: python server.py IP port audio_file"

    # Creamos servidor de eco y escuchamos
    if len(sys.argv) == 4:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
        FILE = sys.argv[3]
        s = SocketServer.UDPServer((IP, PORT), SIPHandler)
        print "Listening...\r\n"
        s.serve_forever()
    else:
        print USAGE
