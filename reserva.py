"""Clase Reserva: integra Cliente + Servicio + duracion + estado."""
from excepciones_personalizadas import (
    DatoInvalidoError, ReservaIncorrectaError,
    OperacionNoPermitidaError, ServicioNoDisponibleError
)
from gestor_logs import registrar_evento, registrar_error

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        if cliente is None or servicio is None:
            raise ReservaIncorrectaError("La reserva requiere un cliente y un servicio validos.")
        if duracion_horas <= 0:
            raise DatoInvalidoError("La duracion de la reserva debe ser mayor a cero.")
        self._id_reserva = id_reserva
        self._cliente = cliente
        self._servicio = servicio
        self._duracion_horas = duracion_horas
        self._estado = "pendiente"
        self._costo_total = 0.0

    @property
    def estado(self): return self._estado

    @property
    def costo_total(self): return self._costo_total

    def confirmar(self):
        if self._estado != "pendiente":
            raise OperacionNoPermitidaError(f"No se puede confirmar una reserva en estado '{self._estado}'.")
        if not self._servicio.disponible:
            raise ServicioNoDisponibleError("El servicio de esta reserva no esta disponible.")
        self._estado = "confirmada"
        self._costo_total = self._servicio.calcular_costo()
        registrar_evento(f"Reserva {self._id_reserva} CONFIRMADA. Costo: ${self._costo_total}")

    def cancelar(self):
        if self._estado in ("cancelada", "procesada"):
            raise OperacionNoPermitidaError(f"No se puede cancelar una reserva en estado '{self._estado}'.")
        self._estado = "cancelada"
        registrar_evento(f"Reserva {self._id_reserva} CANCELADA.")

    def procesar(self):
        if self._estado != "confirmada":
            raise OperacionNoPermitidaError("Solo se puede procesar una reserva CONFIRMADA.")
        self._estado = "procesada"
        registrar_evento(f"Reserva {self._id_reserva} PROCESADA. Cliente: {self._cliente.nombre}")

    def describir(self):
        return (f"Reserva {self._id_reserva} | Cliente: {self._cliente.nombre} | "
                f"Servicio: {self._servicio.nombre} | Duracion: {self._duracion_horas}h | "
                f"Estado: {self._estado} | Costo: ${self._costo_total}")
