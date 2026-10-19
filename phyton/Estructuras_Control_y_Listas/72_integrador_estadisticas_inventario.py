precios = []

for numero_producto in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {numero_producto}: "))
    precios.append(precio)

total = 0
productos_sobre_umbral = 0
producto_mas_costoso = precios[0]

for precio in precios:
    total += precio
    if precio > 50_000:
        productos_sobre_umbral += 1
    if precio > producto_mas_costoso:
        producto_mas_costoso = precio

print("\nReporte del inventario")
print(f"Costo total: ${total:,.2f}")
print(f"Productos que superan $50,000: {productos_sobre_umbral}")
numero_producto_mas_costoso = precios.index(producto_mas_costoso) + 1
print(
    f"Producto más costoso: Producto {numero_producto_mas_costoso} "
    f"(${producto_mas_costoso:,.2f})"
)
