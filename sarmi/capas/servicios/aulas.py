from ... import configuracion
from ..utilidades import horas, listas, textos
from . import superposiciones


def horariosEnAula(oferta, aula, dia):
    """Recibe la oferta, un aula (por ejemplo "7118") y un día (por ejemplo "viernes").
    Busca los horarios que se dictan en esa aula ese día, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: horariosEnAula(oferta, "7118", "viernes") devuelve los horarios de Análisis
    Numérico y de Introducción a la Programación."""
    aula = textos.normalizar(aula)
    dia = textos.normalizar(dia)
    horarios_del_aula = []

    for horario in oferta:
        if textos.normalizar(horario[configuracion.POSICION_DIA]) == dia:
            if textos.contiene(textos.normalizar(horario[configuracion.POSICION_AULA]), aula):
                horarios_del_aula.append(horario)

    return horarios_del_aula


def minutosDeInicio(horario):
    """Recibe un horario.
    Obtiene la hora de inicio y la convierte en minutos desde las 00:00.
    Devuelve la cantidad de minutos correspondiente.
    Ejemplo: si el horario comienza a las 18:30, devuelve 1110."""
    return horas.horaAMinutos(horario[configuracion.POSICION_HORA_INICIO])


def ordenarPorHora(horarios):
    """Recibe una lista de horarios.
    Arma una copia ordenada por hora de inicio, de la más temprana a la más tarde, con el método
    de inserción (sin usar sorted). La lista que recibe no cambia.
    Devuelve la lista ordenada.
    Ejemplo: con un horario que empieza a las 18:00 y otro a las 13:00, devuelve primero el de las 13:00."""
    ordenados = listas.copiarLista(horarios)

    for i in range(1, len(ordenados)):
        horario_actual = ordenados[i]
        minutos_actual = minutosDeInicio(horario_actual)
        j = i - 1

        while j >= 0 and minutosDeInicio(ordenados[j]) > minutos_actual:
            ordenados[j + 1] = ordenados[j]
            j = j - 1

        ordenados[j + 1] = horario_actual

    return ordenados

def aulasDelEdificio(oferta, edificio):
    """OPCIONAL. Recibe la oferta académica y el nombre o número de un edificio.
    Devuelve una lista sin repetidos con todas las aulas presenciales de ese edificio."""
    edificio_buscado = textos.normalizar(edificio)
    aulas = []

    for horario in oferta:
        if horario[configuracion.POSICION_DIA] != configuracion.DIA_VIRTUAL:
            edificio_horario = textos.normalizar(horario[configuracion.POSICION_EDIFICIO])
            aula = horario[configuracion.POSICION_AULA]
            if textos.contiene(edificio_horario, edificio_buscado) and aula != "":
                if not listas.esta(aula, aulas):
                    aulas.append(aula)

    return aulas


def aulasLibres(oferta, dia, horaInicio, horaFin, edificio):
    """OPCIONAL. Recibe la oferta, un día, una franja horaria (horaInicio, horaFin) y un edificio.
    Devuelve la lista de aulas de ese edificio que no tienen clases superpuestas en ese horario."""
    todas_las_aulas = aulasDelEdificio(oferta, edificio)
    dia_buscado = textos.normalizar(dia)
    edificio_buscado = textos.normalizar(edificio)
    ocupadas = []

    for horario in oferta:
        mismo_dia = textos.normalizar(horario[configuracion.POSICION_DIA]) == dia_buscado
        mismo_edificio = textos.contiene(
            textos.normalizar(horario[configuracion.POSICION_EDIFICIO]),
            edificio_buscado
        )
        if mismo_dia and mismo_edificio:
            franja_consulta = ["", "", "", "", "", horario[configuracion.POSICION_DIA], horaInicio, horaFin]
            if superposiciones.seSuperponen(horario, franja_consulta):
                aula = horario[configuracion.POSICION_AULA]
                if not listas.esta(aula, ocupadas):
                    ocupadas.append(aula)

    libres = []
    for aula in todas_las_aulas:
        if not listas.esta(aula, ocupadas):
            libres.append(aula)

    return libres