

# Ejercicio 3: Obtener la fecha y hora actuales en el sistema

from datetime import datetime

ahora = datetime.now()
print(ahora)
print(type(ahora))


fecha = ahora.strftime("%d/%m/%Y") 
hora = ahora.strftime("%H:%M:%S") 
print(fecha)
print(hora)


