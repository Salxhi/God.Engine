contrasena_correcta = "SENA2026"
intentos_maximos = 3

for intento in range(1, intentos_maximos + 1):
    contrasena = input(f"Intento {intento} de {intentos_maximos}. Ingrese la contraseña: ")
    if contrasena == contrasena_correcta:
        print("Acceso Concedido")
        break
    print("Contraseña incorrecta.")
else:
    print("Sistema bloqueado: alerta de seguridad.")
