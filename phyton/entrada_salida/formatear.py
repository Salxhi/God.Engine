# Lista vacía donde guardaremos cada producto
productos = []

# Bucle: se repite 3 veces 
for i in range(1, 4):
    print(f"\n--- Producto {i} ---")
    nombre   = input("Nombre: ").strip()
    cantidad = int(input("Cantidad: "))
    precio   = int(input("Precio unitario: $"))
    subtotal = cantidad * precio

    # Guardamos los 4 valores como una tupla dentro de la lista
    productos.append((nombre, cantidad, precio, subtotal))

# Calcular total general recorriendo la lista
total_general = 0
for p in productos:
    total_general += p[3]   # p[3] es el subtotal

# Imprimir la tabla
print("\n" + "=" * 62)
print(f"{'PRODUCTO':<20} {'CANTIDAD':>2} {'PRECIO':>13} {'SUBTOTAL':>16}")
print("-" * 62)

for nombre, cantidad, precio, subtotal in productos:
    print(f"{nombre:<20} {cantidad:>6} ${precio:>12,.0f} ${subtotal:>15,.0f}")

print("-" * 62)
print(f"{'TOTAL GENERAL':<20} {'':>6} {'':>13} ${total_general:>15,.0f}")
print("=" * 62)