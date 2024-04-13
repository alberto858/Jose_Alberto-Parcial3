import requests

url = "https://ipapi.co/json/"
respuesta = requests.get(url)
    
if respuesta.status_code == 200:
    datos = respuesta.json()
    print("")
    print("Información del sistema operativo:")
    print(f"Nombre: {datos['org']}")
    print(f"País: {datos['country']}")
    print(f"Región: {datos['region']}")
    print(f"Acronimo region: {datos['region_code']}")
    print(f"Idioma: {datos['languages']}")
    print("")

else:
    print(f"Error, no se pudieron validar los datos {respuesta.status_code}")