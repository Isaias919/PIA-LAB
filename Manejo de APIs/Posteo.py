import requests
import json 
#Nombre:Isaias Emiliano Colunga Santos
#Matricula: 1804974
if __name__ == '__main__':
    url = "http://httpbin.org/post"
    argumentos = {'nombre':'Isaias','matricula':'1804974','curso':'Programacion para Ciberseguridad'}
    response = requests.post(url, params=argumentos)
    if response.status_code == 200:
        print(response.content)