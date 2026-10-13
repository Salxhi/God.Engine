edad = int(input("Ingrese su edad: "))
documento = input("¿Cuenta con documento físico? (si/no): ").strip().lower()

if documento == "si" or documento == "sí":
    documento_fisico = True
else:
    documento_fisico = False

if edad >= 18 and documento_fisico:
    print("Acceso permitido.")
else:
    print("Acceso no permitido.")