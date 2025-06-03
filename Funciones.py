from Inputs import get_nombre_participante
from Inputs import pedir_entero_entre
def cargar_participantes(participantes: list) -> None:
    """Carga los nombres de los participantes en la lista."""
    for i in range(5):
        nombre = get_nombre_participante(f"Ingrese nombre del participante {i+1}: ",
        "Error: debe tener mínimo 3 letras y solo letras o espacios.")
        participantes[i][0] = nombre

def cargar_puntuaciones(matriz: list) -> None:
    """Carga las puntuaciones del jurado para cada participante."""
    for i in range(len(matriz)):
        print(f"\nCargando puntuaciones para {matriz[i][0]}:")
        for j in range(1, 4):
            mensaje = f"Ingrese puntuación del jurado {j} (entre 1 y 10): "
            matriz[i][j] = pedir_entero_entre(mensaje, 1, 10)

def mostrar_puntuaciones(participantes: list) -> None:
    """
    Muestra el nombre, puntuaciones individuales y promedio general de cada participante.
    
    Args:
        participantes (list): Matriz con datos de participantes y sus puntuaciones.
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
def mostrar_mayores_a_4(matriz: list) -> None:
    """Muestra participantes con promedio mayor a 4."""
    hay_mayores = False
    print("\nParticipantes con promedio mayor a 4:")
    for i in range(len(matriz)):
        total = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = total / 3
        if promedio > 4:
            hay_mayores = True
            print(f"{matriz[i][0]} - Promedio: {promedio:.2f}")
    if not hay_mayores:
        print("Ningún participante superó el promedio de 4.")
def mostrar_promedios_mayores_a_7(matriz: list) -> None:
    """Muestra los participantes con promedio mayor a 7."""
    print("\nParticipantes con promedio mayor a 7:")
    hay_mayores = False

    for i in range(len(matriz)):
        suma = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = suma / 3

        if promedio > 7:
            hay_mayores = True
            print(f"{matriz[i][0]} - Promedio: {promedio:.2f}")

    if not hay_mayores:
        print("Ningún participante obtuvo promedio mayor a 7.")
def mostrar_promedio_por_jurado(matriz: list) -> None:
    """Muestra el promedio de puntuaciones de cada jurado."""
    print("\nPromedios por jurado:")
    
    for j in range(1, 4): 
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print(f"Jurado {j}: promedio = {promedio:.2f}")
def jurado_mas_estricto(matriz: list) -> None:
    """Muestra cuál o cuáles jurados fueron los más estrictos (menor promedio)."""
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

    #jurado promedio minimo 
    print("\nJurado(s) más estricto(s):")
    for j in range(3):
        if promedios[j] == minimo:
            print(f"Jurado {j + 1} con promedio: {promedios[j]:.2f}")
def buscar_participante(matriz: list) -> None:
    """Permite buscar un participante por nombre y muestra sus datos si existe."""
    nombre_buscado = input("Ingrese el nombre del participante a buscar: ")

    encontrado = False
    for fila in matriz:
        if fila[0].lower() == nombre_buscado.lower():
            # Mostramos datos
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
    """Muestra los 3 participantes con mayor promedio de puntuación."""
    #lista de promedios junto al índice
    promedios = [[0, 0] for _ in range(len(matriz))]  #[promedio, índice]
    
    for i in range(len(matriz)):
        suma = matriz[i][1] + matriz[i][2] + matriz[i][3]
        promedio = suma / 3
        promedios[i][0] = promedio
        promedios[i][1] = i

    top = [-1, -1, -1]  #índices de los 3 mayores promedios
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
