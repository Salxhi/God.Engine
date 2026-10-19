inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el límite final (no incluido): "))
paso = int(input("Ingrese el paso: "))

if paso == 0:
    print("El paso no puede ser cero.")
else:
    for numero in range(inicio, fin, paso):
        print(numero)
