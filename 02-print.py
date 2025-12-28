

# Ejercicio: Exponer el uso básico de la funcion print

# ejemplo basico
print("Este es un ejemplo basico")


# sin un salto de linea
print("Este es un ejemplo basico", end="")
print("Este es un ejemplo basico")
print()


print("Python", "es", "tremendo")
print("Python", "es", "tremendo", sep="-")
print()


print("{} es {}".format("Python", "tremendo"))
print()


numeros = [2, 3, 4, 5, 6, 7]
print(numeros)
print()


capitales = {
    "Colombia": "bogota",
    "Perú" : "Lima",
    "Argentina": "Buenos Aires"    
}
print(capitales)