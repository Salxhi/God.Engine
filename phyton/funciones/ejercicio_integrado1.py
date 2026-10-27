n_insitucion = "SENA"
n_centro = "Centro de servicios financieros"
instructor = "William Ramón Flórez"
n_programa = "ADSO"

def mostrar_encabezado():
    print(f"Institución: {n_insitucion}")
    print(f"Centro de formación: {n_centro}")

def mostrar_detalles_programa():
    print(f"Instructor: {instructor}")
    print(f"Programa: {n_programa}")

def mostrar_pie_pagina():
    print("Gracias por utilizar este programa de funciones en Python")

mostrar_encabezado()
detalles = input("mostrar detalles (s/n): ")
if detalles.lower() == "s":
    mostrar_detalles_programa()
    mostrar_pie_pagina()
elif detalles.lower() == "n":
    mostrar_pie_pagina()
else:
    print("Opción no válida. Por favor, ingrese 's' o 'n'.")