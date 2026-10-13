# Tasas de cambio 
TASA_USD = 4000
TASA_EUR = 4300

# --- Entrada del usuario (solo el monto) ---
monto_cop = float(input("Monto en Pesos Colombianos (COP): "))

# --- Validación ---
if monto_cop < 0:
    print("Error: El monto no puede ser negativo.")
else:
    dolar = monto_cop / TASA_USD
    euro = monto_cop / TASA_EUR

    print("\n--- CONVERSIÓN DE DIVISAS ---")
    print(f"Monto en COP:       ${monto_cop:>15,.2f}")
    print(f"Equivalente en USD: ${dolar:>15,.2f}")
    print(f"Equivalente en EUR: ${euro:>15,.2f}")