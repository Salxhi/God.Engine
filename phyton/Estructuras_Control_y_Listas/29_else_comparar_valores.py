valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

if valor1 > valor2:
    print(f"El mayor es {valor1}.")
elif valor2 > valor1:
    print(f"El mayor es {valor2}.")
else:
    print("Los dos valores son iguales.")
