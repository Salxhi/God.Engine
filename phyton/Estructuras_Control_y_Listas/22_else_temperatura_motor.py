temperatura = float(input("Ingrese la temperatura del motor en °C: "))
limite_seguro = 90

if temperatura <= limite_seguro:
    print("Temperatura normal.")
else:
    print("Sobrecalentamiento: apagado de emergencia.")
