numero = float(input("Ingrese un número mayor o igual a 1: "))

if numero <= 0:
    print("Ingrese un número positivo.")
else:
    while numero >= 1:
        print(f"{numero:g}")
        numero /= 2
