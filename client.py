import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10000))
while True:
	message = raw_input('Message: ')
	if message == 'exit':
		client.close()
		break
	else:
		client.sendall(message)
		if message[:2] == 'dl':
			data = client.recv(1024)
			if data[:5] == 'ERROR':
				print(data)
			else:
				temp = message[2:]
				filename = temp.split('.')[0] + '_dowloaded.' + temp.split('.')[1]  
				with open(filename, 'w') as file:
					file.write(data)
		else:
			print client.recv(1024)

