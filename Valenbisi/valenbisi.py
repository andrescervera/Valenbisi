import requests
from requests.models import Response


URL: str = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20"

print(f'Escribe dirección de la estación')
address = input('')
address = str(address)

respuesta: requests.Response = requests.get(url = URL)
estado: int = respuesta.status_code
datos = respuesta.json()

if estado == 200:
    total_count: str = datos['total_count']
    print(f'{total_count}')
    #number =  
        
        #for i in range(1, total_count + 1):