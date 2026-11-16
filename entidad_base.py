from abc import ABC, abstractmethod
from datetime import datetime

class EntidadBase(ABC):
    """Clase abstracta que representa cualquier entidad del sistema."""
    
    def __init__(self, id_entidad: str):
        self._id = id_entidad.strip()
        self._fecha_creacion = datetime.now()
        self._activo = True

    @property
    def id(self) -> str:
        return self._id

    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion

    @property
    def activo(self) -> bool:
        return self._activo

    def desactivar(self) -> None:
        self._activo = False

    @abstractmethod
    def validar_datos(self) -> bool:
        pass

    @abstractmethod
    def obtener_informacion(self) -> str:
        pass

    def __str__(self) -> str:
        return f"ID: {self._id} | Creado: {self._fecha_creacion.strftime('%d/%m/%Y %H:%M')} | Activo: {self._activo}"
