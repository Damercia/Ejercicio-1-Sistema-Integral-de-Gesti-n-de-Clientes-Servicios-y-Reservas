"""Registra eventos y errores en el archivo sistema.log."""
from datetime import datetime

ARCHIVO_LOG = "sistema.log"

def registrar_evento(mensaje: str) -> None:
    tiempo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{tiempo}] EVENTO: {mensaje}\n")

def registrar_error(error: Exception, contexto: str = "") -> None:
    tiempo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{tiempo}] ERROR ({contexto}): {type(error).__name__}: {error}\n")
