import requests
from requests.models import Response


URL: str = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20"

def num_chistes ():
        numero = input('')
        numero = int(numero)
        if numero <= 5:
            for i in range(1, numero + 1):
                respuesta: requests.Response = requests.get(url = URL)
                estado: int = respuesta.status_code
                datos = respuesta.json()
                if estado == 200:
                    total_count: str = datos['total_count']
                    print(f'El chiste {i} es: {total_count}')
        else:
            print(f"Máximo 5!!! Solicita otro número")
            num_chistes()

num_chistes()