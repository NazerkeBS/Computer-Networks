import socket
import select
import os
import sys, pickle


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 10000))
server_socket.listen(1)

inputs = [server_socket]
outputs = []
timeout=1
while True:
	readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
	
	for s in readable:
		if s is server_socket:    #new client connect
			connection, client_address = server_socket.accept()
			print('New client from %s:%d' % client_address)
			inputs.append(connection)
		else:
			data = s.recv(1024)
			if data:
				if data == 'dir':
					content = os.listdir("C:\\Users\\stud\\Desktop\\computernet")
					#print "Received", data
					c = pickle.dumps(content)
					s.send(c)
				elif data[:2] == 'dl':
					exists = os.path.isfile(data[3:])
					if exists:
						with open(data[3:], 'rb') as f:
							s.sendall(f.read())
					else:
						s.sendall('ERROR. File does not exist')
				elif data[:4] == 'find':
					exists = os.path.isfile(data[5:])
					s.send(str(exists))
			else:
				s.close()
				inputs.remove(s)

	