membresia_activa = input("¿Tiene una membresía VIP activa? (sí/no): ").strip().lower()

if membresia_activa in ("si", "sí"):
    print("Acceso a la sección VIP.")
else:
    print("Acceso a la entrada general.")
