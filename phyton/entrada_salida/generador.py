nombre   = input("Primer nombre: ").strip().lower()
apellido = input("Primer apellido: ").strip().lower()

# Quitar espacios internos por si escriben nombre compuesto ("Juan Carlos")
nombre_limpio   = nombre.replace(" ", "")
apellido_limpio = apellido.replace(" ", "")

# Validación básica: ambos campos deben tener solo letras y no estar vacíos
if not nombre_limpio or not apellido_limpio:
    print("Error: Debe ingresar nombre y apellido.")
elif not nombre_limpio.isalpha() or not apellido_limpio.isalpha():
    print("Error: Solo se permiten letras (sin números ni símbolos).")
else:
    total_letras = len(nombre_limpio) + len(apellido_limpio)
    usuario = nombre_limpio[0] + apellido_limpio + str(total_letras)

    print("\n--- USUARIO GENERADO ---")
    print(f"Nombre completo: {nombre.capitalize()} {apellido.capitalize()}")
    print(f"Usuario:         {usuario}@gmail.com")