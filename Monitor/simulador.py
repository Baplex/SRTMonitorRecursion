from redis_client import guardar_dato
import time
import random


# Funcion para generar Respiraciones por min
def simular():
    respiraciones = random.randint(8, 22)  # Genera un valor aleatorio
    guardar_dato("respiraciones", respiraciones) 

    print(f"Respiración registrada: {respiraciones} resp/min")
    
    time.sleep(2)  # Espera antes de la siguiente llamada
    simular()  # Llamada recursiva en lugar de while True

# First call
simular()
