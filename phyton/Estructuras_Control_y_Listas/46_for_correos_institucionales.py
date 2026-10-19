usuarios = input("Ingrese nombres de usuario separados por coma: ").split(",")

for usuario in usuarios:
    usuario = usuario.strip()
    if usuario:
        print(f"{usuario}@sena.edu.co")
