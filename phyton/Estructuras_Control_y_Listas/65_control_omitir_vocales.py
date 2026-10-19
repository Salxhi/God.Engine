frase = input("Ingrese una frase: ")
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

for caracter in frase:
    if caracter in vocales:
        continue
    print(caracter, end="")

print()
