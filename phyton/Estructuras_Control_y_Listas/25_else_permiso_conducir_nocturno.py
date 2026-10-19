hora = int(input("Ingrese la hora (0 a 23): "))

if not 0 <= hora <= 23:
    print("La hora debe estar entre 0 y 23.")
elif 6 <= hora < 23:
    print("Puede conducir sin restricciones horarias.")
else:
    print("Se requiere autorización para conducir a esta hora.")
