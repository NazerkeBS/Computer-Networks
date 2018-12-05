import socket
import struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 20000))

while True:
	message  = raw_input()
	if message  == 'exit':
		client_socket.close()
		break
	l = message.split()

	packer  = struct.Struct('f 1s f')
	values = (float(l[0]), str(l[1]), float(l[2]))

	packed_data = packer.pack(*values)

	client_socket.sendall(packed_data)

	result =  client_socket.recv(1024) 
   
	if 	message.find(".") == -1:
		print str(int(float(result)))
	else:
		print result
	


