# propuesto3.py

total_cuenta = int(input("Total de la cuenta: "))
propina_pct  = int(input("Porcentaje de propina a dejar (%): "))
personas     = int(input("Número de personas: "))

# Validaciones
if personas <= 0:
    print("Error: El número de personas debe ser al menos 1.")
elif total_cuenta < 0 or propina_pct < 0:
    print("Error: El monto y el porcentaje no pueden ser negativos.")
else:
    propina       = total_cuenta * (propina_pct / 100)
    total_general = total_cuenta + propina
    por_persona   = total_general / personas

    print("\n--- RESUMEN DE LA CUENTA ---")
    print(f"Total cuenta:       ${total_cuenta:>12,.0f}")
    print(f"Propina ({propina_pct:.0f}%):      ${propina:>12,.0f}")
    print(f"Total general:      ${total_general:>12,.0f}")
    print(f"Personas:           {personas:>13}")
    print(f"Cada persona paga:  ${por_persona:>12,.0f}")