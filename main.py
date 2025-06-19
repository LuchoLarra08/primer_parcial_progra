import Funciones

def mostrar_menu():
    """
    Muestra las opciones disponibles del menú.
    """
    print("\n--- Menú de opciones ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Mostrar participantes con promedio mayor a 4")
    print("5. Mostrar participantes con promedio mayor a 7")
    print("6. Mostrar promedio de cada jurado")
    print("7. Mostrar jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Mostrar top 3 participantes")
    print("10. Mostrar participantes ordenados alfabéticamente")
    print("11. Mostrar ganador")
    print("12. Salir")

def main():
    participantes = [["" , 0, 0, 0] for _ in range(5)]  
    cargados_nombres = False
    cargados_puntajes = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            Funciones.cargar_participantes(participantes)
            if all(p[0] != "" for p in participantes):
                cargados_nombres = True
                cargados_puntajes = False
            else:
                print("La carga de participantes no se completó correctamente.")

        elif opcion == "2":
            if not cargados_nombres:
                print("Debe cargar primero los participantes.")
            else:
                Funciones.cargar_puntuaciones(participantes)
                if all(all(isinstance(p, int) and p > 0 for p in participante[1:]) for participante in participantes):
                    cargados_puntajes = True
                else:
                    print("La carga de puntuaciones no se completó correctamente.")

        elif opcion == "3":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.mostrar_puntuaciones(participantes)

        elif opcion == "4":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.mostrar_promedio_mayor_que(participantes, 4)

        elif opcion == "5":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.mostrar_promedio_mayor_que(participantes, 7)

        elif opcion == "6":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.promedio_por_jurado(participantes)

        elif opcion == "7":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.jurado_mas_estricto(participantes)

        elif opcion == "8":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.buscar_participante(participantes)

        elif opcion == "9":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.top_3_participantes(participantes)

        elif opcion == "10":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.ordenar_participantes_alfabeticamente(participantes)

        elif opcion == "11":
            if not cargados_nombres or not cargados_puntajes:
                print("Debe cargar participantes y puntuaciones primero.")
            else:
                Funciones.mostrar_ganador(participantes)

        elif opcion == "12":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

