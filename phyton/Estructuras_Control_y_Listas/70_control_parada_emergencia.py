while True:
    comando = input("Escriba 'continuar' o 'detener': ").strip().lower()
    if comando == "detener":
        print("Parada de emergencia activada.")
        break
    if comando == "continuar":
        print("Sistema en funcionamiento.")
    else:
        print("Comando no reconocido.")
