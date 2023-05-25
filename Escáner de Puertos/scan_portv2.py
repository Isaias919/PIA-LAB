#!/usr/bin/python
#Datos: Isaias Emiliano Colunga Santos 1804974 24/05/23
#P1
#Importamos librerias requeridas
import socket

#P2
#Se define la funcion con la cual se utilizan sockets para probar diferentes puertos
def scan(addr, port):
    #Creando un nuevo socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Estableciendo el timeout para el nuevo objeto tipo socket
    socket.setdefaulttimeout(1)

    #Conexion existosa devuelve 0. Devuelve error en caso contrario
    result = socket_obj.connect_ex((addr, port)) #Direccion y puerto en tupla

    #Se cierra el objeto
    socket_obj.close()

    return result
#P3
#Lista de puertos a escanear
ports=[21, 22, 25, 80]

#P4
#Bucle por todas las ip del rango 192.168.50.*
for i  in range(1,255):
    addr="192.168.50.{}".format(i)
    for port in ports:
        result = scan(addr, port)
        if result == 0:
            print(addr, port, " Ok")
        else:
            print(addr, port, "Failed")