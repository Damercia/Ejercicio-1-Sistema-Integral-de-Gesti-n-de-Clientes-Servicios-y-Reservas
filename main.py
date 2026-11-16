"""
main.py — Simulacion del Sistema Integral de Gestion.
Ejecuta al menos 10 operaciones (validas e invalidas) y genera logs.
El programa NO se detiene ante errores.
"""
from cliente import Cliente
from gestor_logs import registrar_evento, registrar_error
from excepciones_personalizadas import DatoInvalidoError

try:
    from servicio_base import Servicio  # type: ignore
    MOD_SERVICIO_LISTO = True
    registrar_evento("Modulo Servicio cargado correctamente.")
except ImportError as e:
    MOD_SERVICIO_LISTO = False
    registrar_error(e, "Importar servicio_base (aun no entregado)")

try:
    from reserva import Reserva  # type: ignore
    MOD_RESERVA_LISTO = True
    registrar_evento("Modulo Reserva cargado correctamente.")
except ImportError as e:
    MOD_RESERVA_LISTO = False
    registrar_error(e, "Importar reserva (aun no entregado)")

registrar_evento("=== Inicio de la simulacion del sistema ===")

# SIMULACION 1: Cliente valido 
print("\n--- Operacion 1: Crear cliente valido ---")
try:
    c1 = Cliente("100654321", "Karol Rodriguez", "karol@ejemplo.com", "3123456789")
    print(c1.obtener_informacion())
    registrar_evento("Cliente valido creado: " + c1.nombre)
except Exception as e:
    registrar_error(e, "Operacion 1")

# SIMULACION 2: Segundo cliente valido 
print("\n--- Operacion 2: Crear segundo cliente valido ---")
try:
    c2 = Cliente("200987654", "Ana Perez", "ana@ejemplo.com", "3209876543")
    print("Creado:", c2.nombre, "| Valido:", c2.validar_datos())
    registrar_evento("Cliente valido creado: " + c2.nombre)
except Exception as e:
    registrar_error(e, "Operacion 2")

# SIMULACION 3: Nombre muy corto (error) 
print("\n--- Operacion 3: Cliente con nombre corto (debe fallar) ---")
try:
    c3 = Cliente("300111222", "KR", "kr@ejemplo.com", "3111111111")
    print(c3.obtener_informacion())
except ValueError as e:
    print("Error capturado:", e)
    registrar_error(e, "Operacion 3 - nombre corto")

# SIMULACION 4: Correo invalido (error) 
print("\n--- Operacion 4: Cliente con correo invalido (debe fallar) ---")
try:
    c4 = Cliente("400333444", "Luis Gomez", "correo_mal", "3145556666")
    print(c4.obtener_informacion())
except ValueError as e:
    print("Error capturado:", e)
    registrar_error(e, "Operacion 4 - correo invalido")

# SIMULACION 5: Telefono muy corto (error) 
print("\n--- Operacion 5: Cliente con telefono corto (debe fallar) ---")
try:
    c5 = Cliente("500666777", "Marta Ruiz", "marta@ejemplo.com", "12345")
    print(c5.obtener_informacion())
except ValueError as e:
    print("Error capturado:", e)
    registrar_error(e, "Operacion 5 - telefono corto")

# SIMULACION 6: Validar datos de cliente existente 
print("\n--- Operacion 6: Validar datos del cliente 1 ---")
try:
    print("¿Datos validos?", c1.validar_datos())
    registrar_evento("Validacion de cliente 1 exitosa.")
except Exception as e:
    registrar_error(e, "Operacion 6")

#  SIMULACION 7: Desactivar un cliente
print("\n--- Operacion 7: Desactivar cliente 2 ---")
try:
    c2.desactivar()
    print("Cliente 2 activo:", c2.activo)
    registrar_evento("Cliente 2 desactivado.")
except Exception as e:
    registrar_error(e, "Operacion 7")

# SIMULACION 8: Excepcion personalizada 
print("\n--- Operacion 8: Lanzar excepcion personalizada (debe fallar) ---")
try:
    raise DatoInvalidoError("El ID del cliente no puede estar vacio.")
except DatoInvalidoError as e:
    print("Excepcion personalizada capturada:", e)
    registrar_error(e, "Operacion 8 - DatoInvalidoError")

# SIMULACION 9: Intentar usar servicio (modulo pendiente)
print("\n--- Operacion 9: Intentar crear un servicio ---")
try:
    if MOD_SERVICIO_LISTO:
        print("Modulo de servicio disponible: se crearia el servicio aqui.")
        registrar_evento("Servicio creado (modulo listo).")
    else:
        raise ImportError("Modulo servicio_base aun no entregado por el equipo.")
except ImportError as e:
    print("Aviso:", e, "-> El sistema continua.")
    registrar_error(e, "Operacion 9 - servicio pendiente")

# SIMULACION 10: Intentar crear reserva (modulo pendiente) 
print("\n--- Operacion 10: Intentar crear una reserva ---")
try:
    if MOD_RESERVA_LISTO:
        print("Modulo reserva disponible: se crearia la reserva aqui.")
        registrar_evento("Reserva procesada (modulo listo).")
    else:
        raise ImportError("Modulo reserva aun no entregado por el equipo.")
except ImportError as e:
    print("Aviso:", e, "-> El sistema continua.")
    registrar_error(e, "Operacion 10 - reserva pendiente")

registrar_evento("=== Simulacion finalizada. Programa sigue activo ===")
print("\nLas 10 operaciones se ejecutaron. Revisa el archivo sistema.log.")
