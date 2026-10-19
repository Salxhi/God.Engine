numero_secreto = 7
intento = None

while intento != numero_secreto:
    intento = int(input("Adivine el número secreto (entre 1 y 10): "))
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")

print("¡Adivinaste!")
