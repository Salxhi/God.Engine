categoria = input("Categoría de cliente (VIP, regular o nuevo): ").strip().lower()
compra = float(input("Ingrese el valor de la compra: "))

if categoria == "vip":
    descuento = 0.20
elif categoria == "regular":
    descuento = 0.10
elif categoria == "nuevo":
    descuento = 0.05
else:
    descuento = 0
    print("Categoría no reconocida; no se aplica descuento.")

total = compra * (1 - descuento)
print(f"Descuento: {descuento:.0%} | Total a pagar: ${total:,.2f}")
