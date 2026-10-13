correo = input("Ingrese su correo electrónico: ").strip().lower()

# Validaciones (cada una devuelve True/False)
tiene_arroba  = "@" in correo
termina_com   = correo.endswith(".com")
termina_edu   = correo.endswith(".edu.co")
tiene_punto   = "." in correo.split("@")[-1]  # hay un punto después del @?

if tiene_arroba and tiene_punto and (termina_com or termina_edu):
    print(f"✅ El correo '{correo}' tiene un formato VÁLIDO.")
else:
    print(f"❌ El correo '{correo}' tiene un formato INVÁLIDO.")
    if not tiene_arroba:
        print("   - Falta el símbolo '@'.")
    if not tiene_punto:
        print("   - No hay un punto después del '@'.")
    if not (termina_com or termina_edu):
        print("   - Debe terminar en '.com' o '.edu.co'.")