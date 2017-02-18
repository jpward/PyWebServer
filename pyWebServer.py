#!/usr/bin/python
import socket
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="print verbose status messages")
parser.add_option("-p", dest="portnum", default='8888', help="set PORT for server")
(options, args) = parser.parse_args() 

if options.verbose:
  print options

HOST, PORT = '', int(options.portnum)

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
