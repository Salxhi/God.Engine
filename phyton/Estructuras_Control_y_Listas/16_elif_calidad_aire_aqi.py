aqi = int(input("Ingrese el índice de calidad del aire (AQI): "))

if aqi < 0:
    print("El AQI no puede ser negativo.")
elif aqi <= 50:
    print("Calidad del aire: Bueno.")
elif aqi <= 100:
    print("Calidad del aire: Moderado.")
elif aqi <= 150:
    print("Calidad del aire: Dañino para grupos sensibles.")
else:
    print("Calidad del aire: Peligroso.")
