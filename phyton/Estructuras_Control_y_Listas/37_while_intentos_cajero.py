pin_correcto = "2468"
intentos = 0

while intentos < 3:
    pin = input("Ingrese su PIN: ")
    intentos += 1
    if pin == pin_correcto:
        print("Acceso autorizado.")
        break
    print(f"PIN incorrecto. Intentos restantes: {3 - intentos}")
else:
    print("Tarjeta bloqueada por superar los 3 intentos.")
