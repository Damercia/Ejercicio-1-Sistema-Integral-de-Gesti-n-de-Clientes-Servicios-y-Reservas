"""Servicio especializado: Asesoria Especializada. Hereda de Servicio."""
from servicio_base import Servicio
from excepciones_personalizadas import DatoInvalidoError, ServicioNoDisponibleError

class AsesoriaEspecializada(Servicio):
    NIVELES = {"basico": 1.0, "intermedio": 1.5, "avanzado": 2.0}

    def __init__(self, id_servicio, nombre, precio_base, especialista, nivel, horas):
        super().__init__(id_servicio, nombre, precio_base)
        self._especialista = especialista
        self._nivel = nivel.lower().strip()
        self._horas = horas

    def validar_parametros(self):
        if self._nivel not in self.NIVELES:
            raise DatoInvalidoError(f"Nivel invalido. Use: {', '.join(self.NIVELES)}.")
        if self._horas <= 0:
            raise DatoInvalidoError("Las horas de asesoria deben ser mayores a cero.")
        if not self._especialista or not self._especialista.strip():
            raise DatoInvalidoError("El nombre del especialista es obligatorio.")
        return True

    def calcular_costo(self):
        self.validar_parametros()
        if not self.disponible:
            raise ServicioNoDisponibleError(f"La asesoria {self.nombre} no esta disponible.")
        multiplicador = self.NIVELES[self._nivel]
        return round(self.precio_base * self._horas * multiplicador, 2)

    def describir(self):
        return (f"Asesoria: {self.nombre} | Especialista: {self._especialista} | "
                f"Nivel: {self._nivel} | Horas: {self._horas} | Costo: ${self.calcular_costo()}")
