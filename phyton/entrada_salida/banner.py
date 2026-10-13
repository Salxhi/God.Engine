nombre = input("Ingrese el nombre del aprendiz: ").strip()
programa = input("Ingrese el nombre del programa de formación: ").strip()

ancho = 50  # ancho total del recuadro

print("*" * ancho)
print(f"*{'BIENVENIDA'.center(ancho - 2)}*")
print(f"*{('Aprendiz: ' + nombre.upper()).center(ancho - 2)}*")
print(f"*{('Programa: ' + programa).center(ancho - 2)}*")
print("*" * ancho)