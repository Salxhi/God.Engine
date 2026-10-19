while True:
    print("\n1. Saludar\n2. Mostrar una frase\n3. Mostrar un número\n4. Ayuda\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("Python permite resolver problemas paso a paso.")
    elif opcion == "3":
        print("El número seleccionado es 5.")
    elif opcion == "4":
        print("Elija una opción del 1 al 5.")
    elif opcion == "5":
        print("Fin del programa.")
        break
    else:
        print("Opción no válida.")
