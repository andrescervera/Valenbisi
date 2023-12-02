import requests

URL = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

respuesta = requests.get(url=URL)
estado = respuesta.status_code
datos = respuesta.json()

if estado == 200:
    total_count = datos['total_count']
    print(f'Total de estaciones: {total_count}')

    for estacion in datos["results"]:
        id_estacion = estacion["number"]
        direccion = estacion["address"]
        fecha = estacion["updated_at"]
        bicis_disponibles = estacion["available"]
        huecos_libres = estacion["free"]
        
        print(f'Estación: {id_estacion}, Dirección: {direccion}, Bicis Disponibles: {bicis_disponibles}, Huecos Libres: {huecos_libres}, Fecha: {fecha}')
        
        # Aquí puedes realizar la ingesta de datos para cada estación
        # Por ejemplo, almacenar los datos en una base de datos
        
        # Código para realizar la ingesta (ejemplo)
        # insertar_datos(id_estacion, direccion, bicis_disponibles, huecos_libres, fecha)
else:
    print(f"Error: {estado}")