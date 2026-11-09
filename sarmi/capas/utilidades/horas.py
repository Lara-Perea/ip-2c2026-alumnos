MINUTOS_POR_HORA = 60

def horaAMinutos(hora):
    """Recibe una hora escrita como "HH:MM".
    Calcula cuántos minutos pasaron desde las 00:00.
    Devuelve esa cantidad de minutos.
    Ejemplo: horaAMinutos("18:30") devuelve 1110."""
    contador = 0
    acum_hora = ""
    acum_min = ""

    for digito in hora:
        if contador <= 1:
            acum_hora = acum_hora + digito
        elif contador >= 3:
            acum_min = acum_min + digito

        contador = contador + 1

    h_minutos = int(acum_hora) * MINUTOS_POR_HORA
    minutos = int(acum_min)

    return h_minutos + minutos