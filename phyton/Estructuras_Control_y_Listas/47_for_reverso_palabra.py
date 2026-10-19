palabra = input("Ingrese una palabra: ")
reverso = ""

for caracter in palabra:
    reverso = caracter + reverso

print(f"Palabra invertida: {reverso}")
