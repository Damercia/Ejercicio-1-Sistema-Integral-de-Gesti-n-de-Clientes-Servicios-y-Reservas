"""Excepciones personalizadas del sistema."""

class DatoInvalidoError(Exception):
    """Se lanza cuando un dato de entrada no es valido."""
    pass

class ServicioNoDisponibleError(Exception):
    """Se lanza cuando se intenta usar un servicio no disponible."""
    pass

class ReservaIncorrectaError(Exception):
    """Se lanza cuando una reserva tiene parametros incorrectos."""
    pass

class OperacionNoPermitidaError(Exception):
    """Se lanza cuando se intenta una operacion no permitida."""
    pass
