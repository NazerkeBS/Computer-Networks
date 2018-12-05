import socket 
import struct
import os
import os.path

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',10000))
server_socket.listen(1)

connection, client_address = server_socket.accept()
while True:
	data = connection.recv(1024)
	if data:
		if data == 'dir':
			connection.sendall(str(os.listdir(".")))
		elif data[:4] == 'find' and len(data[5:]) != 0:
			connection.sendall(str(os.path.exists(data[5:])))
		elif data[:2] == 'dl' and len(data[3:]) != 0:
			if os.path.exists(data[3:]):
				with open(data[3:]) as f:
					content = f.read()
					connection.sendall(content)
			else:
				connection.sendall('ERROR')
		else:
			connection.sendall('not found')
	else:
		connection.close()