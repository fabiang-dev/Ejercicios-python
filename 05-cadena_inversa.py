
# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres

# Python => nohtyP

cadena = "Python"
print(cadena)

inverso = cadena[::-1]
print(inverso)

inverso2 = ""

# range(inicio, fin, direccion)
for i in range(len(cadena) - 1, -1, -1):
    inverso2 += cadena[i]

print(inverso2)