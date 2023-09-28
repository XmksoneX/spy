from socket import *
#DS= direccion servidor PS=puerto servidor
DS="localhost"
PS= 9099
#SS= socket servidor
SS= socket (AF_INET, SOCK_STREAM)
SS.bind ((DS, PS))
SS.listen ()
print ("Servidor escuchando desde: 127.0.0.1:12345")
while True:
    #SC= Socket conexion MR mensaje recibido
    SC, addr=SS.accept()
    print ("Conexion entrante desde:", addr)
    
    while True:
        MR=SC.recv(4096).decode()
        print ("Cliente: ",MR)
        
        if MR=="salir":
            break
        SC.send(input().encode())
        
    print ("Desconexion del cliente",addr)
    
    SC.close()