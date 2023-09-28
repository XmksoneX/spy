from socket import *
import sys

#SC Socket cliente PS=puerto servidor IP=ip del servidor
ip="localhost"
PS= 9099
SC= socket (AF_INET, SOCK_STREAM)
SC.connect ((ip, PS))
print ("Bienvenido")
print ("Servidor escuchando desde: 127.0.0.1:12345")
print ("si desea salir escriba salir en el chat")
#M=mensaje R=respuesta
while True:
    M=input()
    if M!="salir":
        SC.send (M.encode())
        R=SC.recv (4090).decode()
        print ("servidor: ",R)
    else:
        SC.send (M.encode())
        SC.close()
        sys.exit()
