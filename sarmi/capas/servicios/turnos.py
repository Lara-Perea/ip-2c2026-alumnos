from ... import configuracion
from ..utilidades import horas, textos


def turnoDe(horario):
    """OPCIONAL. Recibe un horario.
    Se fija en qué turno empieza, según TURNOS en configuracion.py.
    Devuelve "mañana", "tarde" o "noche", o "" si el horario es virtual.
    Ejemplo: un horario que empieza a las 18:00 devuelve "noche"."""
    if horario[configuracion.POSICION_DIA] == configuracion.DIA_VIRTUAL:
        return ""
    minutosInicio = horas.horaAMinutos(horario[configuracion.POSICION_HORA_INICIO])
    for nombre, desde, hasta in configuracion.TURNOS:
        if horas.horaAMinutos(desde) <= minutosInicio <= horas.horaAMinutos(hasta):
            return nombre
    return ""


def filtrarPorTurno(horarios, turno):
    """OPCIONAL. Recibe una lista de horarios y un turno ("mañana", "tarde" o "noche").
    Se queda con los horarios que empiezan en ese turno.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Álgebra I y "noche", devuelve el de la COM-02 (miércoles 18:00)."""
    resultado = []
    for horario in horarios:
        if turnoDe(horario) == turno:
            resultado.append(horario)
    return resultado
