entrada = input("Ingrese una nota (0.0 a 5.0): ").replace(",", ".")

try:
    nota = float(entrada)

    if nota < 0.0 or nota > 5.0:
        print(f"❌ Error de rango: la nota {nota} está fuera del rango permitido (0.0 a 5.0).")
    else:
        print(f"✅ Nota registrada correctamente: {nota:.1f}")

except ValueError:
    print(f"❌ Error de tipo: '{entrada}' no es un número válido.")