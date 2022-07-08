import socket            
 
 
s = socket.socket()        
 
 
port = 6666              
 
s.connect(('127.0.0.1', port))
 
print (s.recv(1024).decode())

mensaje = input()
s.send(mensaje.encode())

s.close()  