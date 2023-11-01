from bliblioteca_nba import (limpiar_consola, nba_menu_principal, nba_imprimir_nombre_y_posicion, nba_imprimir_estadisticas_jugador_elegido,buscar_jugador_en_lista,pedir_jugador, guardar_estadisticas_jugador, obtener_datos_jugador_elegido, buscar_jugador, nba_imprimir_logros, obtener_nombre_y_rebotes,calcular_indice_jugador_mas_rebotes,nba_imprimir_nombre_jugador_mas_rebotes,evaluar_si_es_miembro_salon_fama,nba_imprimir_si_es_miembro_o_no,calcular_promedio_puntos,nombres_ordenados_por_promedio_puntos,nba_imprimir_promedio_puntos_y_jugadores, nba_imprimir_promedio_asistencias_y_jugadores)


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
                guardar_estadisticas_jugador(jugador_elegido)
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
            case "0":
                break
            case _:
                print("Opción incorrecta, elija otra: ")
        limpiar_consola()


        