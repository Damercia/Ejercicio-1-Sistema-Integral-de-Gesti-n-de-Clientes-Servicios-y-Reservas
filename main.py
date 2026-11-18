"""
main.py — Simulacion del Sistema Integral de Gestion de Clientes, Servicios y Reservas.
Software FJ. Ejecuta 12 operaciones (validas e invalidas) y registra todo en sistema.log.
El programa NO se detiene ante errores. Incluye try/except/else/finally y encadenamiento.
"""
from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializadaxc
from reserva import Reserva
from gestor_logs import registrar_evento, registrar_error
from excepciones_personalizadas import (
    SistemaError, DatoInvalidoError, ServicioNoDisponibleError,
    ReservaIncorrectaError, OperacionNoPermitidaError
)

registrar_evento("=== INICIO DE SIMULACION DEL SISTEMA ===")
exitos = 0
fallos = 0

def registrar_resultado(ok, contexto):
    global exitos, fallos
    if ok:
        exitos += 1
        registrar_evento("OK: " + contexto)
    else:
        fallos += 1

# Operacion 1: Cliente valido 
print("\n--- Operacion 1: Crear cliente valido ---")
try:
    c1 = Cliente("100654321", "Karol Rodriguez", "karol@ejemplo.com", "3123456789")
    print(c1.obtener_informacion())
    registrar_resultado(True, "Cliente valido creado: " + c1.nombre)
except SistemaError as e:
    registrar_error(e, "Operacion 1")
    registrar_resultado(False, "Operacion 1")

#  Operacion 2: Segundo cliente valido 
print("\n--- Operacion 2: Crear segundo cliente valido ---")
try:
    c2 = Cliente("200987654", "Ana Perez", "ana@ejemplo.com", "3209876543")
    print("Creado:", c2.nombre, "| Valido:", c2.validar_datos())
    registrar_resultado(True, "Cliente valido creado: " + c2.nombre)
except SistemaError as e:
    registrar_error(e, "Operacion 2")
    registrar_resultado(False, "Operacion 2")

# Operacion 3: Cliente con nombre corto (error esperado) 
print("\n--- Operacion 3: Cliente con nombre corto (debe fallar) ---")
try:
    Cliente("300111222", "KR", "kr@ejemplo.com", "3111111111")
except DatoInvalidoError as e:
    print("Error capturado (DatoInvalidoError):", e)
    registrar_error(e, "Operacion 3 - nombre corto")
    registrar_resultado(False, "Operacion 3 (error controlado)")

# Operacion 4: Cliente con correo invalido (error esperado) 
print("\n--- Operacion 4: Cliente con correo invalido (debe fallar) ---")
try:
    Cliente("400333444", "Luis Gomez", "correo_mal", "3145556666")
except DatoInvalidoError as e:
    print("Error capturado (DatoInvalidoError):", e)
    registrar_error(e, "Operacion 4 - correo invalido")
    registrar_resultado(False, "Operacion 4 (error controlado)")

# Operacion 5: ReservaSala valida 
print("\n--- Operacion 5: Crear ReservaSala valida ---")
try:
    sala = ReservaSala("S-001", "Sala de Juntas Principal", 50.0, 20, "19:00", 2)
    print(sala.describir())
    print("Costo con impuestos:", sala.calcular_con_impuestos())
    registrar_resultado(True, "ReservaSala creada: " + sala.nombre)
except SistemaError as e:
    registrar_error(e, "Operacion 5")
    registrar_resultado(False, "Operacion 5")

# Operacion 6: AlquilerEquipo valido 
print("\n--- Operacion 6: Crear AlquilerEquipo valido ---")
try:
    equipo = AlquilerEquipo("E-001", "Proyector HD", 15.0, "Proyeccion", 10)
    print(equipo.describir())
    print("Costo con descuento 10%:", equipo.calcular_con_descuento(0.10))
    registrar_resultado(True, "AlquilerEquipo creado: " + equipo.nombre)
except SistemaError as e:
    registrar_error(e, "Operacion 6")
    registrar_resultado(False, "Operacion 6")

# Operacion 7: AsesoriaEspecializada valida 
print("\n--- Operacion 7: Crear AsesoriaEspecializada valida ---")
try:
    asesoria = AsesoriaEspecializada("A-001", "Consultoria Python", 40.0, "Ing. Torres", "avanzado", 3)
    print(asesoria.describir())
    registrar_resultado(True, "Asesoria creada: " + asesoria.nombre)
except SistemaError as e:
    registrar_error(e, "Operacion 7")
    registrar_resultado(False, "Operacion 7")

# Operacion 8: Servicio con precio negativo (error) + try/except/else/finally 
print("\n--- Operacion 8: Servicio con precio negativo (debe fallar) ---")
try:
    ReservaSala("S-002", "Sala Error", -10.0, 10, "10:00", 1)
except DatoInvalidoError as e:
    print("Error capturado:", e)
    registrar_error(e, "Operacion 8 - precio negativo")
    registrar_resultado(False, "Operacion 8 (error controlado)")
else:
    print("No hubo error (inesperado).")
finally:
    print("Bloque finally: la Operacion 8 siempre llega hasta aqui.")
    registrar_evento("Operacion 8 finalizada (finally ejecutado).")

# Operacion 9: Asesoria con nivel invalido (error esperado)
print("\n--- Operacion 9: Asesoria con nivel invalido (debe fallar) ---")
try:
    AsesoriaEspecializada("A-002", "Asesoria X", 30.0, "Ing. X", "maestro", 2)
except DatoInvalidoError as e:
    print("Error capturado:", e)
    registrar_error(e, "Operacion 9 - nivel invalido")
    registrar_resultado(False, "Operacion 9 (error controlado)")

# Operacion 10: Reserva exitosa (confirmar + procesar) 
print("\n--- Operacion 10: Reserva exitosa (confirmar y procesar) ---")
try:
    r1 = Reserva("R-001", c1, sala, 2)
    r1.confirmar()
    r1.procesar()
    print(r1.describir())
    registrar_resultado(True, "Reserva R-001 procesada exitosamente")
except SistemaError as e:
    registrar_error(e, "Operacion 10")
    registrar_resultado(False, "Operacion 10")

# Operacion 11: Encadenamiento de excepciones 
print("\n--- Operacion 11: Procesar reserva sin confirmar (debe fallar) ---")
try:
    try:
        r2 = Reserva("R-002", c2, equipo, 5)
        r2.procesar()  # error: no esta confirmada
    except OperacionNoPermitidaError as e:
        raise ReservaIncorrectaError("No se puede procesar una reserva sin confirmar.") from e
except ReservaIncorrectaError as e:
    print("Error encadenado capturado:", e)
    print("Causa original:", e.__cause__)
    registrar_error(e, "Operacion 11 - encadenamiento (causa: " + str(e.__cause__) + ")")
    registrar_resultado(False, "Operacion 11 (error controlado)")

# Operacion 12: Servicio no disponible + segundo encadenamiento 
print("\n--- Operacion 12: Reservar servicio no disponible (debe fallar) ---")
try:
    try:
        equipo.desactivar()
        r3 = Reserva("R-003", c1, equipo, 3)
        r3.confirmar()
    except ServicioNoDisponibleError as e:
        raise ReservaIncorrectaError("La reserva no se puede confirmar.") from e
except ReservaIncorrectaError as e:
    print("Error encadenado capturado:", e)
    print("Causa original:", e.__cause__)
    registrar_error(e, "Operacion 12 - servicio no disponible (causa: " + str(e.__cause__) + ")")
    registrar_resultado(False, "Operacion 12 (error controlado)")

# Final
registrar_evento("=== SIMULACION FINALIZADA: " + str(exitos) + " exitosas, " + str(fallos) + " controladas ===")
print("\n=== RESUMEN: " + str(exitos) + " exitosas, " + str(fallos) + " errores controlados ===")
print("Revisa el archivo sistema.log para ver el registro completo.")
print("El programa termina normalmente, sin interrupciones.")
