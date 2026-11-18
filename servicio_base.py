"""Clase abstracta Servicio — base para todos los servicios de Software FJ.
Karol Rodriguez — Modulo servicio_base.
"""
from abc import ABC, abstractmethod
from excepciones_personalizadas import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(ABC):
    """Clase abstracta que representa un servicio general."""

    def __init__(self, id_servicio: str, nombre: str, precio_base: float):
        if not id_servicio or not id_servicio.strip():
            raise DatoInvalidoError("El id del servicio no puede estar vacio.")
        if precio_base < 0:
            raise DatoInvalidoError("El precio base no puede ser negativo.")
        self._id_servicio = id_servicio.strip()
        self._nombre = nombre.strip()
        self._precio_base = float(precio_base)
        self._disponible = True

    # --- Propiedades (encapsulamiento) ---
    @property
    def id_servicio(self): return self._id_servicio

    @property
    def nombre(self): return self._nombre

    @property
    def precio_base(self): return self._precio_base

    @property
    def disponible(self): return self._disponible

    def desactivar(self):
        """Marca el servicio como no disponible."""
        self._disponible = False

    # --- Metodos abstractos (debe implementarlos cada servicio hijo) ---
    @abstractmethod
    def calcular_costo(self, *args, **kwargs) -> float:
        """Calcula el costo final del servicio."""
        pass

    @abstractmethod
    def describir(self) -> str:
        """Describe el servicio con sus caracteristicas."""
        pass

    @abstractmethod
    def validar_parametros(self, *args, **kwargs) -> bool:
        """Valida los parametros propios del servicio."""
        pass

    # --- Metodos con variantes (sobrecarga por parametros opcionales) ---
    def calcular_con_impuestos(self, impuesto: float = 0.19) -> float:
        """Costo base mas impuestos (19% por defecto)."""
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio {self._nombre} no esta disponible.")
        return round(self._precio_base * (1 + impuesto), 2)

    def calcular_con_descuento(self, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        """Costo con descuento opcional y luego impuestos."""
        if not (0 <= descuento <= 1):
            raise DatoInvalidoError("El descuento debe estar entre 0 y 1.")
        subtotal = self._precio_base * (1 - descuento)
        return round(subtotal * (1 + impuesto), 2)

    def __str__(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"Servicio: {self._nombre} | ID: {self._id_servicio} | Precio base: ${self._precio_base} | {estado}"
