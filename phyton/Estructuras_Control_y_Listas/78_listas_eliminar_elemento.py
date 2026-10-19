productos = ["Monitor", "Mouse", "Teclado", "Audífonos"]
producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")

if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"Inventario actualizado: {productos}")
else:
    print("El producto no está en la lista.")
