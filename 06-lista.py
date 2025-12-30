
# Ejercicio 6: Obtener un conjunto de números separados por coma y crear un lista


entrada = input("Escriba varios números separados por coma: ")
print(type(entrada))

# convertir en una lista de string
numeros = entrada.split(",")
print(type(numeros))
print(numeros)


# convertir en una lista de numeros
numeros2 = [int(n) for n in numeros]
print(numeros2)


