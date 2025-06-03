def es_letra_o_espacio(c):
    """Devuelve True si el carácter es una letra (mayúscula o minúscula) o espacio, sino False."""
    codigo = ord(c)
    if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122) or codigo == 32:
        return True
    else:
        return False

def es_nombre_valido(nombre):
    """Valida que el nombre tenga al menos 3 caracteres y solo letras o espacios."""
    if len(nombre) < 3:
        return False
    for caracter in nombre:
        if not es_letra_o_espacio(caracter):
            return False
    return True

def get_nombre_participante(mensaje, mensaje_error):
    """Pide un nombre y lo valida según los criterios."""
    while True:
        nombre = input(mensaje).strip()
        if es_nombre_valido(nombre):
            return nombre
        else:
            print(mensaje_error)

def pedir_entero_entre(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo (inclusive) y valida el ingreso."""
    while True:
        valor = input(mensaje)

        solo_digitos = True
        for c in valor:
            if ord(c) < 48 or ord(c) > 57:
                solo_digitos = False
                break
        if not solo_digitos:
            print(f"Error: debe ingresar un número entero entre {minimo} y {maximo}.")
            continue

        numero = 0
        for c in valor:
            numero = numero * 10 + (ord(c) - 48)  
        if numero >= minimo and numero <= maximo:
            return numero
        else:
            print(f"Error: debe ingresar un número entero entre {minimo} y {maximo}.")


