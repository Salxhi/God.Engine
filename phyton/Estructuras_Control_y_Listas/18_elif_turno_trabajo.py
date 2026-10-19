hora = int(input("Ingrese la hora de ingreso (0 a 23): "))

if not 0 <= hora <= 23:
    print("La hora debe estar entre 0 y 23.")
elif hora < 12:
    print("Turno: Mañana.")
elif hora < 18:
    print("Turno: Tarde.")
else:
    print("Turno: Noche.")
