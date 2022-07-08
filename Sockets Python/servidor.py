import socket            
 
 
s = socket.socket()        
print ("Se creo el socket")
 
port = 6666              
 
s.bind(('', port))        
print ("socket conectado al puerto %s" %(port))
 
s.listen(5)    
print ("escuchando")          
 
while True:
 
  c, addr = s.accept()    
  print ('se conecto desde', addr )
  c.send('Conectado correctamente'.encode())
  c.close()
  break