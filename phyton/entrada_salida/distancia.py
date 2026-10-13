distancia = float(input("Distancia del viaje (km): "))
velocidad = float(input("Velocidad promedio (km/h): "))

if velocidad <= 0:
    print("Error: La velocidad debe ser mayor que cero.")
elif distancia < 0:
    print("Error: La distancia no puede ser negativa.")
else:
    tiempo_total_h = distancia / velocidad      # horas en decimal
    horas   = int(tiempo_total_h)                # parte entera
    minutos = round((tiempo_total_h - horas) * 60)  # residuo * 60

    # Ajuste por redondeo: si minutos da 60, hay que sumar 1 hora
    if minutos == 60:
        horas += 1
        minutos = 0

    print("\n--- TIEMPO ESTIMADO DE VIAJE ---")
    print(f"Distancia:  {distancia:,.2f} km")
    print(f"Velocidad:  {velocidad:,.2f} km/h")
    print(f"Tiempo:     {horas} horas y {minutos} minutos")