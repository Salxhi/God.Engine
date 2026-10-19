bytes_archivo = float(input("Ingrese el tamaño del archivo en bytes: "))

if bytes_archivo < 0:
    print("El tamaño no puede ser negativo.")
elif bytes_archivo < 1024:
    print(f"Tamaño: {bytes_archivo:.2f} bytes")
elif bytes_archivo < 1024**2:
    print(f"Tamaño: {bytes_archivo / 1024:.2f} KB")
elif bytes_archivo < 1024**3:
    print(f"Tamaño: {bytes_archivo / 1024**2:.2f} MB")
else:
    print(f"Tamaño: {bytes_archivo / 1024**3:.2f} GB")
