"""Excepciones personalizadas del sistema.
Todas heredan de una clase base comun: SistemaError."""

class SistemaError(Exception):
    """Clase base comun para todas las excepciones del sistema."""
    pass

class DatoInvalidoError(SistemaError):
    """Dato de entrada no valido."""
    pass

class ServicioNoDisponibleError(SistemaError):
    """Servicio no disponible."""
    pass

class ReservaIncorrectaError(SistemaError):
    """Reserva con parametros incorrectos."""
    pass

class OperacionNoPermitidaError(SistemaError):
    """Operacion no permitida."""
    pass
