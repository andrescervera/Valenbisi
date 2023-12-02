import requests
from requests.models import Response


URL: str = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20"

print(f'Escribe dirección de la estación')
address = input('')
address = str(address)

respuesta: requests.Response = requests.get(url=URL)
estado: int = respuesta.status_code
datos = respuesta.json()

if estado == 200:
    total_count: str = datos['total_count']
    print(f'Total de estaciones: {total_count}')

    #total de direcciones disponibles
    print("Direcciones disponibles:")
    for estacion in datos["results"]:
        print(estacion["address"])

    for estacion in datos["results"]:
        if estacion["address"] == address:
            numero_estacion = estacion["number"]
            fecha = estacion["updated_at"]
            bicis_disponibles = estacion["available"]
            huecos_libres = estacion["free"]
            print(f'El número de la estación "{address}" es: {numero_estacion}, tiene {bicis_disponibles} bicis disponibles, hay {huecos_libres} huecos libres a fecha {fecha}')
            break
    else:
        print(f"No se encontró la estación con la dirección '{address}'")
else:
    print(f"Error: {estado}")