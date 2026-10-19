viento_kmh = float(input("Ingrese la velocidad del viento en km/h: "))

if viento_kmh < 0:
    print("La velocidad no puede ser negativa.")
elif viento_kmh < 119:
    print("No alcanza la categoría de huracán.")
elif viento_kmh <= 153:
    print("Huracán categoría 1.")
elif viento_kmh <= 177:
    print("Huracán categoría 2.")
elif viento_kmh <= 208:
    print("Huracán categoría 3.")
elif viento_kmh <= 251:
    print("Huracán categoría 4.")
else:
    print("Huracán categoría 5.")
