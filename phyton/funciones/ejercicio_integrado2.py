mision = "cumplir la función que le corresponde al Estado de invertir en el desarrollo social y técnico de los trabajadores colombianos."
vision = "ser una entidad de excelencia en la formación integral de los aprendices, con calidad y pertinencia, que contribuya al desarrollo del país."
contacto = "https://www.sena.edu.co/es-co/Paginas/contactenos.aspx"
def opcion_mision():
    print(f"Misión: {mision}")
def opcion_vision():
    print(f"Visión: {vision}")
def opcion_contacto():
    print(f"Contacto: {contacto}")

if __name__ == "__main__":
    print("Opciones disponibles:")
    print("1. Misión")
    print("2. Visión")
    print("3. Contacto")
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    
    if opcion == "1":
        opcion_mision()
    elif opcion == "2":
        opcion_vision()
    elif opcion == "3":
        opcion_contacto()
    else:
        print("Opción no válida.")