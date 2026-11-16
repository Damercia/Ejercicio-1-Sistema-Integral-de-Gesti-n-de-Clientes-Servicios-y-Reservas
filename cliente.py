from entidad_base import EntidadBase
import re

class Cliente(EntidadBase):
    """Clase que representa a un cliente con encapsulacion y validaciones estrictas."""
    
    def __init__(self, id_entidad: str, nombre: str, correo: str, telefono: str):
        super().__init__(id_entidad)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        nombre_limpio = valor.strip()
        if len(nombre_limpio) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", nombre_limpio):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        self._nombre = nombre_limpio

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        correo_limpio = valor.strip().lower()
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.fullmatch(patron, correo_limpio):
            raise ValueError("El correo electronico tiene un formato invalido.")
        self._correo = correo_limpio

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        tel_limpio = re.sub(r"\D", "", valor)
        if len(tel_limpio) < 7 or len(tel_limpio) > 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 digitos.")
        self._telefono = tel_limpio

    def validar_datos(self) -> bool:
        try:
            return all([
                len(self._id) > 0,
                len(self._nombre) >= 3,
                "@" in self._correo,
                len(self._telefono) >= 7
            ])
        except Exception:
            return False

    def obtener_informacion(self) -> str:
        return (
            f"=== DATOS DEL CLIENTE ===\n"
            f"Identificacion: {self._id}\n"
            f"Nombre:         {self._nombre}\n"
            f"Correo:         {self._correo}\n"
            f"Telefono:       {self._telefono}\n"
            f"Activo:         {'Si' if self._activo else 'No'}\n"
            f"Fecha registro: {self._fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}"
        )

    def __repr__(self) -> str:
        return f"Cliente('{self._id}', '{self._nombre}', '{self._correo}')"
