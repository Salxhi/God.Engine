contrasena_correcta = "SENA2026"

for intento in range(1, 4):
    contrasena = input(f"Intento {intento} de 3. Ingrese la contraseña: ")
    if contrasena == contrasena_correcta:
        print("Acceso concedido.")
        break
    print("Contraseña incorrecta.")
else:
    print("Se agotaron los intentos.")
