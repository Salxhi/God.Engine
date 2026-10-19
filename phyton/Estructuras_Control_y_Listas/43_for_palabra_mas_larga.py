palabras = input("Ingrese palabras separadas por coma: ").split(",")
palabra_mas_larga = ""

for palabra in palabras:
    palabra = palabra.strip()
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

if palabra_mas_larga:
    print(f"La palabra más larga es: {palabra_mas_larga}")
else:
    print("No se ingresaron palabras.")
