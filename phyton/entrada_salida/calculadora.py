valor_compra = float(input("Ingrese el valor de compra del equipo informático: "))
vida_util = int(input("Ingrese los años de vida útil: "))

if vida_util <= 0:
    print("Los años de vida útil deben ser mayores que 0.")
else:
    depreciacion_anual = valor_compra / vida_util

    # Formato de moneda colombiana
    valor_formateado = f"{depreciacion_anual:,.0f}"
    valor_formateado = valor_formateado.replace(",", "X")
    valor_formateado = valor_formateado.replace(".", ",")
    valor_formateado = valor_formateado.replace("X", ".")

    print(f"Depreciación anual: {valor_formateado} COP")