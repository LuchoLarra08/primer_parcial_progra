from Funciones import cargar_puntuaciones, cargar_participantes, mostrar_puntuaciones,  mostrar_mayores_a_4, mostrar_promedios_mayores_a_7, mostrar_promedio_por_jurado, jurado_mas_estricto, buscar_participante, top_3_participantes

participantes = [[""] * 4 for _ in range(5)]

participantes_cargados = False
puntuaciones_cargadas = False  #bandera puntuaciones

while True:
    print("\n--- MENÚ ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio mayor a 4")    
    print("5. Participantes con promedio mayor a 7")
    print("6. Mostrar promedio de cada jurado")
    print("7. Mostrar jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3 participantes con mayor puntaje promedio")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        cargar_participantes(participantes)
        participantes_cargados = True
        puntuaciones_cargadas = False  
        print("Participantes cargados correctamente.")
        for fila in participantes:
            print(fila)

    elif opcion == "2":
        if participantes_cargados:
            cargar_puntuaciones(participantes)
            puntuaciones_cargadas = True
            print("Puntuaciones cargadas correctamente.")
        else:
            print("Primero debe cargar los nombres de los participantes.")

    elif opcion == "3":
        if participantes_cargados and puntuaciones_cargadas:
            mostrar_puntuaciones(participantes)
        else:
            print("Debe cargar participantes y puntuaciones antes de mostrar.")

    elif opcion == "4":
        if participantes_cargados and puntuaciones_cargadas:
            mostrar_mayores_a_4(participantes)
        else:
            print("Debe cargar participantes y puntuaciones antes de continuar.")

    elif opcion == "5":
        if participantes_cargados and puntuaciones_cargadas:
            mostrar_promedios_mayores_a_7(participantes)
        else:
            print("Primero debe cargar los participantes y sus puntuaciones.")

    elif opcion == "6":
        if participantes_cargados and puntuaciones_cargadas:
            mostrar_promedio_por_jurado(participantes)
        else:
            print("Primero debe cargar los participantes y sus puntuaciones.")

    elif opcion == "7":
        if participantes_cargados and puntuaciones_cargadas:
            jurado_mas_estricto(participantes)
        else:
            print("Primero debe cargar los participantes y sus puntuaciones.")

    elif opcion == "8":
        if participantes_cargados and puntuaciones_cargadas:
            buscar_participante(participantes)
        else:
            print("Primero debe cargar los participantes y sus puntuaciones.")

    elif opcion == "9":
        if participantes_cargados and puntuaciones_cargadas:
            top_3_participantes(participantes)
        else:
            print("Primero debe cargar los participantes y sus puntuaciones.")


    elif opcion == "0":
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")

