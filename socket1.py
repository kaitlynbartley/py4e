import socket #import socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#make a socket
mysock.connect(('data.pr4e.org', 80)) #connect socket to destination across internet, specify which port
#making a socket connection = 3 lines of code ("dials the phone")
#telnet = way to connect to any server insecurely 
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#encode = prepare for sending
mysock.send(cmd)

while True:
	data = mysock.recv(512)#receive up to 512 characters
	if (len(data) < 1):
		break
	print(data.decode())#if we get data, decode it
mysock.close()
#http request in python, send or receive data 
#request response cycle in python 