import requests

api_url = "https://restcountries.com/v3.1/name/"

pais_name = "canada"

url = f"{api_url}{pais_name}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("")
    print(f"Nombre: {data[0]['name']['official']}")
    print(f"Capital: {data[0]['capital'][0]}")
    print(f"Población: {data[0]['population']}")
    print(f"Región: {data[0]['region']}")
    print(f"Subregión: {data[0]['subregion']}")
    print("")

else:
    print(f"Error: {response.status_code}")
