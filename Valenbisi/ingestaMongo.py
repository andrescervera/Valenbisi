import requests
from pymongo import MongoClient
import pandas as pd

username = "admin"
password = "admin01"
database_name = "estaciones_valenbisi"
collection_name = "estaciones"

client = MongoClient("mongodb://admin:admin01@localhost:27017/?authSource=admin")

db = client['estaciones_valenbisi']  # Reemplazar 'nombre_base_datos' por el nombre de tu base de datos
collection = db['estaciones']  # Nombre de la colección donde se guardarán los datos

result = collection.delete_many({}) #borrar base de datos

URL = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

respuesta = requests.get(url=URL)
estado = respuesta.status_code
datos = respuesta.json()

if estado == 200:
    total_count = datos['total_count']
    print(f'Total de estaciones: {total_count}')
    
    # Ordenar datos por id_estacion ascendente
    sorted_data = sorted(datos["results"], key=lambda x: x["number"])

    for estacion in sorted_data:
        id_estacion = estacion["number"]
        direccion = estacion["address"]
        fecha = estacion["updated_at"]
        bicis_disponibles = estacion["available"]
        huecos_libres = estacion["free"]
        
        print(f'Estación: {id_estacion}, Dirección: {direccion}, Bicis Disponibles: {bicis_disponibles}, Huecos Libres: {huecos_libres}, Fecha: {fecha}')
        
        # Insertar datos en la colección 'estaciones'
        data = {
            "id_estacion": id_estacion,
            "direccion": direccion,
            "bicis_disponibles": bicis_disponibles,
            "huecos_libres": huecos_libres,
            "fecha": fecha
        }
        
        # Utilizar update_one para insertar o actualizar
        collection.update_one(
            {"_id": id_estacion},
            {"$set": data},
            upsert=True
        )

    print("Datos insertados en la base de datos MongoDB.")
    
    #Recuperamos toda la info para el posterior estudio y generamos un dataframe
    estudio = collection.find()
    df = pd.DataFrame(list(estudio))
    
    #Lo guardamos en un archivo csv
    df.to_csv('datos_estaciones.csv', index=False)

else:
    print(f"Error: {estado}")