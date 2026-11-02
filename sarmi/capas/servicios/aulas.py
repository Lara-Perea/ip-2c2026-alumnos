from ... import configuracion
from ..utilidades import horas, listas, textos


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