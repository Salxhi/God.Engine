# Evaluación de requisitos para crédito
ingresos_mensuales = 2500.0
tiene_deudas = False
credito_aprobado = ingresos_mensuales > 2000 and not tiene_deudas
print(f"Ingresos mensuales: ${ingresos_mensuales:.2f} | ¿Tiene deudas?: {tiene_deudas} | ¿Crédito aprobado?: {credito_aprobado}")
