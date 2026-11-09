from ... import configuracion
from ..utilidades import horas

def seSuperponen(horarioA, horarioB):
    """Recibe dos horarios.
    Se fija si los dos son presenciales, son el mismo día y sus horas se cruzan.
    Si uno termina justo cuando empieza el otro (de 14 a 18 y de 18 a 22), no se superponen.
    Devuelve True si se superponen y False si no.
    Ejemplo: un viernes de 18:00 a 22:00 y un viernes de 20:00 a 22:00 se superponen: devuelve True."""
    diaA = horarioA[configuracion.POSICION_DIA]
    diaB = horarioB[configuracion.POSICION_DIA]

    if diaA == configuracion.DIA_VIRTUAL or diaB == configuracion.DIA_VIRTUAL:
        return False

    hora_inicioA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_INICIO])
    hora_finA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_FIN])

    hora_inicioB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_INICIO])
    hora_finB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_FIN])

    if (diaA == diaB) and (hora_inicioA < hora_finB) and (hora_inicioB < hora_finA):
        return True
    
    return False


def buscarSuperposiciones(horariosA, horariosB):
    """Recibe dos listas de horarios (por ejemplo, los de dos comisiones).
    Compara cada horario de la primera lista con cada horario de la segunda.
    Devuelve una lista de pares [horarioA, horarioB] que se superponen, o una lista vacía si no hay ninguno.
    Ejemplo: con [viernesDe18a22] y [viernesDe20a22, lunesDe18a22] devuelve [[viernesDe18a22, viernesDe20a22]]."""
    superposiciones = []
    for elemento in horariosA:
        for item in horariosB:
            if seSuperponen(elemento, item):
                superposiciones.append([elemento, item])    
    return superposiciones
