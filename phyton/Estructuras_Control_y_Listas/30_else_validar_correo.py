correo = input("Ingrese una dirección de correo electrónico: ").strip()

if "@" in correo:
    print("El correo contiene el carácter @.")
else:
    print("El correo no contiene el carácter @.")
