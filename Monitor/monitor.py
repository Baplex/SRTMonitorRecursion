from redis_client import obtener_dato
import time


#Set de condiciones de min y max respiraciones permitidas
MIN_RESP = 12
MAX_RESP = 18

#Funcion de coleccion de valores respiratorios y alarma
def monitorear():
    respiraciones = obtener_dato("respiraciones")

    if respiraciones:
        respiraciones = int(respiraciones)
        estado = "Normal"

        if respiraciones < MIN_RESP:
            estado = "RESPIRACIÓN BAJA!!"
        elif respiraciones > MAX_RESP:
            estado = "RESPIRACIÓN ALTA!!"

        print(f" Respiraciones: {respiraciones} resp/min - {estado}")

    time.sleep(2)  # Espera antes de la siguiente llamada
    monitorear()  # Llamada recursiva 

# First call a la funcion
monitorear()
