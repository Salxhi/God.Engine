# Cálculo de propinas
cuenta_total = 80000.0
propina_10 = cuenta_total * 0.10
propina_15 = cuenta_total * 0.15
total_10 = cuenta_total + propina_10
total_15 = cuenta_total + propina_15

print(f"Cuenta: ${cuenta_total:.2f}")
print(f"Con 10% de propina: ${total_10:.2f}")
print(f"Con 15% de propina: ${total_15:.2f}")
