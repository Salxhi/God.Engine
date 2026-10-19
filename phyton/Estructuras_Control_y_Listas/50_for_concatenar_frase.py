palabras = input("Ingrese las palabras de una frase separadas por coma: ").split(",")
frase = ""

for palabra in palabras:
    palabra = palabra.strip()
    if palabra:
        if frase:
            frase += " "
        frase += palabra

print(frase)
