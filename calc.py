import socket
import struct

server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 20001))
server_socket.listen(1)

connection, client_address = server_socket.accept()

while True:
	data  = connection.recv(1024)
	unpacker  = struct.Struct('f 1s f')
	unpacked_data = unpacker.unpack(data)

	result  = eval(str(unpacked_data[0]) + str(unpacked_data[1]) + str(unpacked_data[2]))

	connection.sendall(str(result))

