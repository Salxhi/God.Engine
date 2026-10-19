medalla = input("Ingrese la medalla obtenida (oro, plata o bronce): ").strip().lower()

if medalla == "oro":
    puntos = 100
elif medalla == "plata":
    puntos = 50
elif medalla == "bronce":
    puntos = 20
else:
    puntos = 0
    print("Medalla no reconocida.")

print(f"Puntaje asignado: {puntos}")
