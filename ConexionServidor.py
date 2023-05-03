# escribe-html.py

import webbrowser
import socket
import sys

f = open('holamundo.html','w')

webbrowser.open_new_tab('holamundo.html')

HOST = '172.26.1.194'    # The remote host
PORT = 80              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    f.write('Recivido', repr(data))

f.close()
