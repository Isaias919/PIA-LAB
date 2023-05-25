# Importamos fernet desde cryptography

from cryptography.fernet import Fernet
#Definicion de la funcion genwrite que genera una llave para cifrarlo
def genwrite():
    key = Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)

#Llamamos a la funcion para generar el archivo "pass.key"
# que contiene la llave
genwrite()

#Dfincion de la funcion call_key con la cual leemos
# el contenido del archivo "pass.key"
def call_key():
    return open("pass.key","rb").read()
#Ahora ciframos el mensaje almacenado y codificado previamente
key = call_key()
banner = "Hola,usuario, seas bienvenido a la practica 7 ".encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)
#
#Ahora deciframos el mensaje previamente cifrado
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)
#
#Fin del script
#Isaias Emiliano Colunga Santos - 1804974
#Lab. Ciber Seguridad
# Grupo 063