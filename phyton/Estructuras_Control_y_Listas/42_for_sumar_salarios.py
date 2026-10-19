salarios = []

for indice in range(5):
    salario = float(input(f"Ingrese el salario {indice + 1}: "))
    salarios.append(salario)

total = 0
for salario in salarios:
    total += salario

print(f"Sumatoria de salarios: ${total:,.2f}")
