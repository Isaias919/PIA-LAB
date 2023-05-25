#Isaias Emiliano Colunga Santos - 1804974 - 04/05/23
from email.message import EmailMessage
import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
#Iniciar sesion
x = str(input("Escribe tu correo electronico: "))
y = str(input("Escribe tu clave de acceso o contraseña asignada: "))
conn.login(x,y)

#Datos de envio
z = str(input("Escribe el correo del destinatario: "))
remitente = x
destinatario = z #gerardo.bernal@uanl.edu.mx

#Cuerpo del mensaje
mensaje = "<H2><strong>Practica 12</strong><br></H2> <p>Ejercicio de la practica 12 para envio de correos</p> " \
          "<p><strong>Alumno:</strong> Isaias Emiliano Colunga Santos</p> " \
          "<p><strong>Matricula:</strong> 1804974</p>"

#Estructura del mensaje del correo
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Prueba de envio (script Python) - 1804974"
#Convertir a HTML
email.set_content(mensaje, subtype="html")
#Adjuntar la imagen
with open("fcfm_cool.png", "rb") as f:
    email.add_attachment(
        f.read(),
        filename="fcfm_cool.png",
        maintype="image",
        subtype="png"
    )
#Enviar mensaje
conn.sendmail(remitente, destinatario, email.as_string())
#Cerrar sesion
conn.quit()