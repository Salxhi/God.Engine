ingreso = float(input("Ingrese el ingreso mensual del hogar: "))
gastos = float(input("Ingrese los gastos mensuales del hogar: "))

if gastos > ingreso:
    print("Alerta: los gastos superan el ingreso familiar.")
else:
    print("El presupuesto está equilibrado.")
