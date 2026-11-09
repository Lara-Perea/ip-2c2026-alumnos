

def normalizar(texto): #######CHEQUEAR#################
    """Recibe un texto.
    Lo pasa a minúsculas y le saca las tildes (ver LETRAS_CON_TILDE en configuracion.py).
    Devuelve el texto nuevo.
    Ejemplo: normalizar("Introducción a la PROGRAMACIÓN") devuelve "introduccion a la programacion"."""
    LETRAS_CON_TILDE = "áéíóúü" 
    LETRAS_SIN_TILDE = "aeiouu" 
    nuevo_texto = ""
    texto = texto.lower()
    for letra in texto:
        if letra in LETRAS_CON_TILDE:
            contador = 0
            for tilde in LETRAS_CON_TILDE:
                if letra == tilde:
                    nuevo_texto = nuevo_texto + LETRAS_SIN_TILDE[contador] 
                contador = contador + 1 #HACE CICLOS INNECESARIOS
        else:
            nuevo_texto = nuevo_texto + letra
    return nuevo_texto



def contiene(texto, buscado):
    """Recibe dos textos: texto y buscado.
    Se fija si buscado aparece en alguna parte de texto.
    Devuelve True si aparece y False si no.
    Ejemplo: contiene("introduccion a la programacion", "program") devuelve True."""
    if buscado in texto: 
            return True
    
    return False


def extraerNumero(texto):
    """Recibe un texto.
    Junta los dígitos que aparecen en el texto y los convierte en número.
    Devuelve ese número, o -1 si el texto no tiene dígitos.
    Ejemplo: extraerNumero("COM-07") devuelve 7."""
    numeros = "0123456789"
    nuevo_num = ""
    for digito in texto:
        if digito in numeros:
            nuevo_num = nuevo_num + digito 
    if nuevo_num == "":
        return -1
    
    return int(nuevo_num)
