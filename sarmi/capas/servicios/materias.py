from ... import configuracion
from ..utilidades.textos import normalizar, extraerNumero, contiene
from ..utilidades.listas import esta

def valoresDistintos(horarios, posicion):
    """Recibe una lista de horarios y una posición (ver POSICION_... en configuracion.py).
    Junta el dato que está en esa posición en cada horario, sin repetir.
    Devuelve la lista de esos valores, en el orden en que aparecen.
    Ejemplo: con los horarios de Introducción a la Programación y POSICION_COMISION,
    devuelve ["COM-01", "COM-02", "COM-03", ...]."""
    valores = []
    for hora in horarios:
        dato = hora[posicion]
        if not esta(dato, valores): 
            valores.append(dato)
    return valores



def buscarMateria(oferta, nombre):
    """Recibe la oferta y el nombre de una materia, o una parte (por ejemplo "programacion").
    Busca los horarios cuya materia contiene ese nombre, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: buscarMateria(oferta, "programacion") devuelve los horarios de Introducción a la
    Programación, Programación I, Programación II y otras."""
    lista_horarios = []
    nombre = normalizar(nombre)

    for horas in oferta:
        materia = normalizar(horas[configuracion.POSICION_MATERIA])

        if contiene(materia, nombre):
            lista_horarios.append(horas)

    return lista_horarios

def filtrarMateriaExacta(horarios, nombre):
    """Recibe una lista de horarios y el nombre de una materia.
    Se queda con los horarios cuya materia se llama exactamente así, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: si están los horarios de Programación I y de Programación II, con "programación i"
    devuelve solo los de Programación I."""
    lista_hora = []
    nombre = normalizar(nombre)
    for hora in horarios:
        materia = normalizar(hora[configuracion.POSICION_MATERIA])

        if nombre == materia:
            lista_hora.append(hora)

    return lista_hora


def filtrarPorComision(horarios, comision):
    """Recibe una lista de horarios y una comisión, escrita como sea ("7", "07", "COM-07" o "comisión 7").
    Se queda con los horarios de esa comisión, comparando solo el número.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Introducción a la Programación y "7", devuelve los dos horarios
    de la COM-07: el del viernes y el virtual."""
    comision = extraerNumero(comision)
    lista_hora = []
    for horario in horarios:
        comision_horario = horario[configuracion.POSICION_COMISION]
        if comision == extraerNumero(comision_horario):
            lista_hora.append(horario)
    return lista_hora
