numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
opcion = input("Operación (1 sumar, 2 restar, 3 multiplicar, 4 dividir): ")

if opcion == "1":
    print(f"Resultado: {numero1 + numero2}")
elif opcion == "2":
    print(f"Resultado: {numero1 - numero2}")
elif opcion == "3":
    print(f"Resultado: {numero1 * numero2}")
elif opcion == "4":
    if numero2 == 0:
        print("No se puede dividir entre cero.")
    else:
        print(f"Resultado: {numero1 / numero2}")
else:
    print("Opción no válida.")
