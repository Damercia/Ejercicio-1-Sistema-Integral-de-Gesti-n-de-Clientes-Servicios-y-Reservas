"""Servicio especializado: Alquiler de Equipos. Hereda de Servicio."""
from servicio_base import Servicio
from excepciones_personalizadas import DatoInvalidoError, ServicioNoDisponibleError

class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, tipo_equipo, horas_alquiler):
        super().__init__(id_servicio, nombre, precio_base)
        self._tipo_equipo = tipo_equipo
        self._horas_alquiler = horas_alquiler

    def validar_parametros(self):
        if not self._tipo_equipo or not self._tipo_equipo.strip():
            raise DatoInvalidoError("El tipo de equipo no puede estar vacio.")
        if self._horas_alquiler <= 0:
            raise DatoInvalidoError("Las horas de alquiler deben ser mayores a cero.")
        return True

    def calcular_costo(self):
        self.validar_parametros()
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El equipo {self.nombre} no esta disponible.")
        costo = self.precio_base * self._horas_alquiler
        if self._horas_alquiler > 8:  # descuento por alquiler prolongado
            costo *= 0.90
        return round(costo, 2)

    def describir(self):
        return (f"AlquilerEquipo: {self.nombre} | Tipo: {self._tipo_equipo} | "
                f"Horas: {self._horas_alquiler} | Costo: ${self.calcular_costo()}")
