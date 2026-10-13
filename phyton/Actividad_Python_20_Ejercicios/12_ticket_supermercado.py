# Ticket de compra de supermercado
precio_producto1 = 3.50
cantidad_producto1 = 2
precio_producto2 = 2.50
cantidad_producto2 = 3

total_producto1 = precio_producto1 * cantidad_producto1
total_producto2 = precio_producto2 * cantidad_producto2
total_pagar = total_producto1 + total_producto2

print(f"Producto 1: ${precio_producto1:.2f} x {cantidad_producto1} = ${total_producto1:.2f}")
print(f"Producto 2: ${precio_producto2:.2f} x {cantidad_producto2} = ${total_producto2:.2f}")
print(f"TOTAL A PAGAR: ${total_pagar:.2f}")
