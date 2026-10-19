numeros = [12, -5, 8, -2, 15]
suma = 0

for numero in numeros:
    if numero < 0:
        continue
    suma += numero

print(f"Suma de los números no negativos: {suma}")
