edad = int(input("Ingrese la edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 13:
    print("Clasificación: Niño.")
elif edad < 18:
    print("Clasificación: Adolescente.")
elif edad < 60:
    print("Clasificación: Adulto.")
else:
    print("Clasificación: Adulto Mayor.")
