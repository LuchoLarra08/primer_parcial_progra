def validar_numero(numero: str, minimo: int, maximo: int) -> bool:
    """
    Valida si el número ingresado es un entero dentro del rango especificado.
    """
    if numero.isdigit():
        valor = int(numero)
        return minimo <= valor <= maximo
    return False

def validar_nombre(nombre: str) -> bool:
    """
    Valida si el nombre tiene al menos 3 caracteres y solo contiene letras y espacios.
    """
    nombre_sin_espacios = nombre.replace(" ", "")
    return len(nombre) >= 3 and nombre_sin_espacios.isalpha()



def pedir_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    """
    Solicita al usuario un número entero dentro de un rango, con intentos limitados.
    """
    contador = 1
    resultado = None
    while contador <= reintentos:
        entrada = input(mensaje)
        if validar_nombre(entrada, minimo, maximo):
            resultado = int(entrada)
            break
        else:
            print(f"{mensaje_error} * Intentos restantes: {reintentos - contador} * \n")
            contador += 1
    return resultado


def obtener_nombre_participante(mensaje: str, error_msg: str, reintentos: int) -> str | None:
    """
    Solicita al usuario ingresar un nombre válido (al menos 3 letras, solo letras y espacios),
    con cantidad limitada de intentos.
    """
    contador = 1
    nombre_valido = None

    while contador <= reintentos:
        nombre = input(mensaje).strip()
        if validar_nombre(nombre):
            nombre_valido = nombre
            break
        else:
            print(f"{error_msg} * Intentos restantes: {reintentos - contador} * \n")
            contador += 1

    return nombre_valido

