notas = [45, 72, 88, 50, 61]
cantidad_mayores_50 = 0

for nota in notas:
    if nota > 50:
        cantidad_mayores_50 += 1

print(f"Cantidad de notas mayores a 50: {cantidad_mayores_50}")
