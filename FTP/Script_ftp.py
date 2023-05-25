#
#
#
# Script para transferencia de FTP
# Objetivo: Conectarse a servidor ftp y hacer un upload de un archivo
# 18-04-23 v1 Isaias Emiliano Colunga Santos
#
# Importando modulo ftp
from ftplib import FTP
#
# Estableciendo conexion a servidor
ftp = FTP("192.168.48.128")
print("Estableciendo conexion...\n")

# Iniciar sesion con el Usuario
ftp.login("doomslayer", "1804974")

# Entra a la carpeta "Upload" de la IP
ftp.cwd("upload")

# Listar el contenido de "Upload"
print("Lista de la carpeta 'Upload'")
ftp.retrlines("LIST")

# Poner el archivo ADVERTENCIA.txt en carpeta "Upload" de la IP
with open("ADVERTENCIA.txt", "rb") as text_file:
    ftp.storlines("STOR ADVERTENCIA.txt", text_file)

# Cerrar conexion con la IP o servidor
print("\nCerrando conexion...")
ftp.quit()