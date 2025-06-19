from Inputs import obtener_nombre_participante, pedir_entero

def cargar_participantes(participantes: list) -> None:
    """
    Carga los nombres de cinco participantes en la lista proporcionada.
    Args:
        participantes (list): Lista donde cada elemento es otra lista con nombre y puntuaciones.
        Debe tener 5 elementos inicialmente con estructura [nombre, 0, 0, 0].
    """
    for i in range(5):
        nombre = obtener_nombre_participante(
            f"Ingrese nombre del participante {i+1}: ",
            "Error: debe tener mínimo 3 letras y solo letras o espacios.",
            reintentos=3
        )
        if nombre is None:
            print("No se ingresó un nombre válido después de varios intentos. Se interrumpe la carga")
            return
        participantes[i][0] = nombre

def cargar_puntuaciones(matriz: list) -> None:
    """
    Carga las puntuaciones que cada jurado otorga a cada participante.

    Args:
        matriz (list): Lista con la estructura [nombre, puntaje_jurado1, puntaje_jurado2, puntaje_jurado3].
    """
    for i in range(len(matriz)):
        print(f"\nCargando puntuaciones para {matriz[i][0]}:")
        for j in range(1, 4):
            mensaje = f"Ingrese puntuación del jurado {j} (entre 1 y 10): "
            puntaje = pedir_entero(
                mensaje,
                "Error: debe ser un número entre 1 y 10.",
                1,
                10,
                reintentos=3
            )
            if puntaje is None:
                print("No se ingresó un puntaje válido después de varios intentos. Se interrumpe la carga.")
                return
            matriz[i][j] = puntaje

def mostrar_puntuaciones(participantes: list) -> None:
    """
    Muestra los datos de cada participante con sus puntuaciones individuales y promedio.

    Args:
        participantes (list): Lista con datos de participantes y puntuaciones.
    """
    for i in range(len(participantes)):
        nombre = participantes[i][0]
        total = 0
        for j in range(1, 4):
            total += participantes[i][j]
        promedio = total / 3
        print(f"Participante {i+1}: {nombre}")
        for j in range(1, 4):
            print(f"  Jurado {j}: {participantes[i][j]}")
        print(f"  Promedio: {promedio:.2f}")
        print("--------------------------")

def mostrar_promedio_mayor_que(matriz: list, limite: float) -> None:
    """
    Muestra los participantes cuyo promedio es mayor a un valor dado.

    Args:
        matriz (list): Lista con datos de participantes.
        limite (float): Valor límite para mostrar participantes con promedio mayor.
    """
    hay_mayores = False
    print(f"\nParticipantes con promedio mayor a {limite}:")
    for i in range(len(matriz)):
        suma = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = suma / 3
        if promedio > limite:
            hay_mayores = True
            print(f"{matriz[i][0]} - Promedio: {promedio:.2f}")
    if not hay_mayores:
        print(f"Ningún participante superó el promedio de {limite}.")

def promedio_por_jurado(matriz: list) -> None:
    """
    Calcula y muestra el promedio de puntuaciones otorgadas por cada jurado.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    print("\nPromedios por jurado:")
    for j in range(1, 4):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print(f"Jurado {j}: promedio = {promedio:.2f}")

def jurado_mas_estricto(matriz: list) -> None:
    """
    Identifica y muestra cuál o cuáles jurados otorgaron los puntajes promedio más bajos.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    promedios = [0] * 3
    for j in range(3):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j + 1]
        promedio = suma / len(matriz)
        promedios[j] = promedio
    minimo = promedios[0]
    for i in range(1, 3):
        if promedios[i] < minimo:
            minimo = promedios[i]

    print("\nJurado(s) más estricto(s):")
    for j in range(3):
        if promedios[j] == minimo:
            print(f"Jurado {j + 1} con promedio: {promedios[j]:.2f}")

def buscar_participante(matriz: list) -> None:
    """
    Permite buscar un participante por nombre y muestra sus datos si existe.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    nombre_buscado = input("Ingrese el nombre del participante a buscar: ").strip()
    encontrado = False
    for fila in matriz:
        if fila[0].lower() == nombre_buscado.lower():
            suma = fila[1] + fila[2] + fila[3]
            promedio = suma / 3
            print("\n--- Datos del participante ---")
            print(f"Nombre: {fila[0]}")
            print(f"Puntuación Jurado 1: {fila[1]}")
            print(f"Puntuación Jurado 2: {fila[2]}")
            print(f"Puntuación Jurado 3: {fila[3]}")
            print(f"Promedio: {promedio:.2f}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un participante con ese nombre.")

def top_3_participantes(matriz: list) -> None:
    """
    Muestra los tres participantes con mayor puntaje promedio.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    promedios = [[0, 0] for _ in range(len(matriz))]  # [promedio, índice]
    for i in range(len(matriz)):
        suma = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = suma / 3
        promedios[i][0] = promedio
        promedios[i][1] = i

    top = [-1, -1, -1]
    for _ in range(3):
        mayor = -1
        indice_mayor = -1
        for i in range(len(promedios)):
            if promedios[i][0] != -1 and (mayor == -1 or promedios[i][0] > mayor):
                mayor = promedios[i][0]
                indice_mayor = i
        if indice_mayor != -1:
            for j in range(3):
                if top[j] == -1:
                    top[j] = indice_mayor
                    break
            promedios[indice_mayor][0] = -1

    print("\n--- Top 3 participantes con mayor promedio ---")
    for i in range(3):
        if top[i] != -1:
            fila = matriz[top[i]]
            suma = fila[1] + fila[2] + fila[3]
            promedio = suma / 3
            print(f"{i+1}. {fila[0]} - Promedio: {promedio:.2f}")

def ordenar_participantes_alfabeticamente(matriz: list) -> None:
    """
    Ordena alfabéticamente a los participantes y muestra sus datos.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    n = len(matriz)
    for i in range(n-1):
        for j in range(n - i - 1):
            if matriz[j][0].lower() > matriz[j+1][0].lower():
                temp = matriz[j]
                matriz[j] = matriz[j+1]
                matriz[j+1] = temp
    print("\nParticipantes ordenados alfabéticamente:")
    for i in range(n):
        fila = matriz[i]
        suma = fila[1] + fila[2] + fila[3]
        promedio = suma / 3
        print(f"{fila[0]} - Jurado 1: {fila[1]}, Jurado 2: {fila[2]}, Jurado 3: {fila[3]}, Promedio: {promedio:.2f}")

def mostrar_ganador(matriz: list) -> None:
    """
    Muestra el participante ganador de la competencia o informa si hay empate.

    Args:
        matriz (list): Lista con datos de participantes y puntuaciones.
    """
    max_promedio = -1
    ganadores = []
    for i in range(len(matriz)):
        suma = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = suma / 3
        if promedio > max_promedio:
            max_promedio = promedio
            ganadores = [matriz[i][0]] 
        elif promedio == max_promedio:
            ganadores = ganadores + [matriz[i][0]] 
    if len(ganadores) == 1:
        print(f"\nEl ganador es: {ganadores[0]} con promedio {max_promedio:.2f}")
    else:
        print("\nHay empate entre los siguientes participantes:")
        for g in ganadores:
            print(f"- {g}")
        print("Se requiere desempate.")
