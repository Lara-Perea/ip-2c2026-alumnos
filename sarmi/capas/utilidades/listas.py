def esta(elemento, lista):
    """Recibe un elemento y una lista.
    Se fija si el elemento aparece en la lista.
    Devuelve True si aparece y False si no.
    Ejemplo: esta("COM-07", ["COM-01", "COM-07"]) devuelve True."""
    for item in lista:        #modifico Lara como prueba
        if elemento == item:  #modifico Lara como prueba
            return True       #modifico Lara como prueba


    return False


def copiarLista(lista):
    """Recibe una lista.
    Arma una lista nueva con los mismos elementos, en el mismo orden.
    Devuelve la lista nueva: si después se modifica la copia, la original no cambia.
    Ejemplo: copiarLista([1, 2, 3]) devuelve otra lista [1, 2, 3]."""
    nueva_lista = []                  #modifico Lara como prueba
    for item in lista:                #modifico Lara como prueba
        nueva_lista.append(item)      #modifico Lara como prueba
    
    
    return nueva_lista