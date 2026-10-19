numeros = [12, -4, 0, 7, -9, 3]
positivos = []
negativos = []

for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
