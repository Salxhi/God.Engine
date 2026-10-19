inventario = [("Teclado", 12), ("Mouse", 4), ("Monitor", 8)]
stock_minimo = 5

for producto, cantidad in inventario:
    if cantidad < stock_minimo:
        print(f"{producto}: reabastecer (stock {cantidad}).")
    else:
        print(f"{producto}: stock suficiente ({cantidad}).")
