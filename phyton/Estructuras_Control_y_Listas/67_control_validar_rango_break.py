while True:
    numero = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        break
    print("Valor fuera de rango. Intente nuevamente.")

print(f"Número válido: {numero}")
