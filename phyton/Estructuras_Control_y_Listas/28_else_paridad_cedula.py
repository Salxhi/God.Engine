numero_cedula = int(input("Ingrese el último dígito de la cédula: "))

if numero_cedula % 2 == 0:
    print("Turno de pico y cédula para números pares.")
else:
    print("Turno de pico y cédula para números impares.")
