from cliente import Cliente

print("=== Prueba de la clase Cliente ===\n")

try:
    # Cliente valido
    cliente1 = Cliente("1065236474", "Karol Rodriguez", "karol@gmail.com", "3161387042")
    print(cliente1.obtener_informacion())
    print(f"¿Datos validos? {cliente1.validar_datos()} \n")

    # Cliente con error (nombre corto)
    cliente2 = Cliente("200987654", "KR", "karol2@gmail.com", "3209876543")
    print(cliente2.obtener_informacion())

except ValueError as e:
    print(f" Error capturado: {e}")

print("\n=== Programa sigue funcionando ===")
