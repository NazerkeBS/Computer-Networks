import socket
import select
import struct

from collections import OrderedDict

proxy_client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_client_socket.bind(('localhost', 20000))
proxy_client_socket.listen(1)

inputs = [proxy_client_socket]
outputs  = []
timeout  = 1

dict_data  = OrderedDict()

proxy_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_server_socket.connect(('localhost', 20001))

while True:
	readable, writable, exceptional = select.select(inputs,outputs, inputs,timeout)
	for s in readable:
		if s is proxy_client_socket:
			connection, client_address = proxy_client_socket.accept()
			print('New client from %s:%d' % client_address)
			inputs.append(connection)
		else:
			data = s.recv(1024)

			if dict_data.has_key(data):
				print "cached"
				s.sendall(str(dict_data[data]))
			else: 
				print "not cached"
				proxy_server_socket.sendall(data)

				result = proxy_server_socket.recv(1024)

				if len(dict_data) == 5:
					dict_data.popitem(last = False)
				dict_data[data] = result

				s.sendall(str(result))














