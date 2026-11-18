"""Servicio especializado: Reserva de Salas. Hereda de Servicio."""
from servicio_base import Servicio
from excepciones_personalizadas import DatoInvalidoError, ServicioNoDisponibleError

class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, capacidad, hora_inicio, duracion_horas):
        super().__init__(id_servicio, nombre, precio_base)
        self._capacidad = capacidad
        self._hora_inicio = hora_inicio
        self._duracion_horas = duracion_horas

    def validar_parametros(self):
        if self._capacidad <= 0:
            raise DatoInvalidoError("La capacidad de la sala debe ser mayor a cero.")
        if self._duracion_horas <= 0:
            raise DatoInvalidoError("La duracion debe ser mayor a cero horas.")
        try:
            hora = int(self._hora_inicio.split(":")[0])
            if not (0 <= hora <= 23):
                raise DatoInvalidoError("La hora de inicio es invalida.")
        except (ValueError, IndexError):
            raise DatoInvalidoError("Formato de hora invalido. Use HH:MM.")
        return True

    def calcular_costo(self):
        self.validar_parametros()
        if not self.disponible:
            raise ServicioNoDisponibleError(f"La sala {self.nombre} no esta disponible.")
        costo = self.precio_base * self._duracion_horas
        hora = int(self._hora_inicio.split(":")[0])
        if 18 <= hora <= 21:  # hora pico
            costo *= 1.25
        return round(costo, 2)

    def describir(self):
        return (f"ReservaSala: {self.nombre} | Capacidad: {self._capacidad} personas | "
                f"Inicio: {self._hora_inicio} | Duracion: {self._duracion_horas}h | "
                f"Costo: ${self.calcular_costo()}")
