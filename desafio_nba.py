from bliblioteca_nba import *


jugador_elegido = {}

def nba_app(lista_jugadores:list[object]):
    while True:
        opcion_elegida = nba_menu_principal()
        match opcion_elegida:
            case "A":
                nba_imprimir_nombre_y_posicion(lista_jugadores)
            case "B":
                jugador = (buscar_jugador_en_lista(lista_jugadores,pedir_jugador()))
                nba_imprimir_estadisticas_jugador_elegido(jugador)
                jugador_elegido = obtener_datos_jugador_elegido(jugador)
                guardar_estadisticas_jugador(f"{ROOT_DIR}estadisticas{jugador_elegido.get('nombre')}",jugador_elegido,pedir_desicion())
            case "C":
                nba_imprimir_logros(buscar_jugador(lista_jugadores))
            case "D":
                nba_imprimir_promedio_puntos_y_jugadores(calcular_promedio_puntos(lista_jugadores),nombres_ordenados_por_promedio_puntos(lista_jugadores))
            case "E":
                nba_imprimir_si_es_miembro_o_no(evaluar_si_es_miembro_salon_fama(buscar_jugador(lista_jugadores)))
            case "F":
                nba_imprimir_nombre_jugador_mas_rebotes(obtener_nombre_y_rebotes(calcular_indice_jugador_mas_rebotes(lista_jugadores)))
            case "G":
                nba_imprimir_promedio_asistencias_y_jugadores(lista_jugadores)
            case "H":
                guardar_estadisticas_jugador(f"{ROOT_DIR}",crear_datos_promedio_asistencias_partido(lista_jugadores),pedir_desicion())
            case "I":
                nba_crear_archivo_json(armar_ruta_json(ROOT_DIR,pedir_nombre_ruta()),crear_datos_promedio_asistencias_partido(lista_jugadores))
            case "J":
                nba_guardar_promedio_asistencias_db(f"{ROOT_DIR}promedio_asistencias_nba.db",crear_datos_promedio_asistencias_partido(lista_jugadores))
            case "K":
                nba_listar_por_robos_mas_bloqueos(lista_jugadores)
            case "L":
                nba_listar_por_robos_mas_bloqueos(lista_jugadores,True)
            case "M":
                nba_listar_por_robos_mas_bloqueos(lista_jugadores,False,True)
            case "N":
                nba_crear_posiciones(f"{ROOT_DIR}posiciones_nba.db",obtener_posiciones(lista_jugadores))
            case "0":
                break
            case _:
                print("Opción incorrecta, elija otra: ")
        limpiar_consola()


        