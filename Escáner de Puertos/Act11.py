#Datos: Isaias Emiliano Colunga Santos 1804974 24/05/23
import nmap
import pprint
scaner = nmap.PortScanner()

#Menu del programa
def Menu():
    Kon = False
    while Kon == False:
        print("==============> Menu <==============")
        print("1.Escaneo UDP\n2.Escaneo Completo\n3.Deteccion de sistema operativo\n4.Escaneo de red con ping\n5.Salir")
        x = int(input("Escribe la opcion que necesites: "))

        if x == 1:
            print("\nOpcion seleccionada: Escaneo UDP")
            IP = str(input("Introduce una IP valida a analizar:\n "))   #Por una razon extraña el escaneo UDP 
            print(scaner.scan(IP, '1-1024', '-v -sU' ))  #-sU UDP       #tarda demasiado, pero juro que si me jalo :c
            print(scaner[IP].all_protocols())
            print(scaner[IP]['udp'].keys())


        elif x == 2:
            print("\nOpcion seleccionada: Escaneo Completo")
            IP = str(input("Introduce una IP valida a analizar:\n "))
            print("Escaneo de TCP")
            print(scaner.scan(IP, '1-1024', '-v -sS' )) 
            print("\nEscaneo de UDP")
            print(scaner.scan(IP, '1-1024', '-v -sU' )) 


        elif x == 3:
            print("\nOpcion seleccionada: Deteccion del S.O")
            IP = str(input("Introduce una IP valida a analizar:\n "))
            pprint.pprint(scaner.scan(IP, '1-1024', '-A' ))

        elif x == 4:
            print("\nOpcion seleccionada: Escaneo de red con ping")
            IP = str(input("Introduce una IP valida a analizar:\n "))
            pprint.pprint(scaner.scan(IP, arguments='-sP -PA'))

        elif x == 5:
            print("\nOpcion seleccionada: Salir")
            Kon = True
        else:
            print("\n-------< OPCION INVALIDA >-------\nIntente denuevo")
        print("====================================\n")

Menu()



    
