import socket
import struct
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 10000))

while True:
	message = raw_input('command: ')
	if message == 'exit':
		client_socket.close()
		break
	if message == 'dir':
		client_socket.sendall(message)
		print (client_socket.recv(1024))
	elif message[:4] == 'find' and len(message[5:]) != 0:
		client_socket.sendall(message)
		print client_socket.recv(1024)
	elif message[:2] == 'dl' and len(message[3:]) != 0:
		client_socket.sendall(message)
		content = client_socket.recv(1024)
		if content == 'ERROR':
			print 'error , try again'
			client_socket.close()
			break
		file = message[3:] + "_downloaded" 
		with open(file ,'w') as f:
			f.write(content)
		print 'succcessfully written to the file'
	else:
		print "invalid command"
		client_socket.close()
		break
