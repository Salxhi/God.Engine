saldo = float(input("Ingrese el saldo inicial: "))

while saldo > 0:
    monto = float(input("Ingrese el monto de la transacción: "))
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        continue
    if monto > saldo:
        print(f"Transacción de ${monto:.2f} rechazada: saldo insuficiente.")
        continue
    saldo -= monto
    print(f"Se descontaron ${monto:.2f}. Saldo: ${saldo:.2f}")
    if saldo == 0:
        print("Saldo agotado; se detienen las transacciones.")
