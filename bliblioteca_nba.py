import os, re
from  equipo import Equipo
from jugador import Jugador
from copy import deepcopy

ROOT_DIR = './datos/'
equipo = Equipo()
equipo.leer_json(f'{ROOT_DIR}dream_team.json')

def imprimir_dato(dato:str)->None:
    #recibe: un string
    #Imprime el dato recibido
    #Retorno: no tiene
    print(dato)

def imprimir_menu()->None:
    #Imprime el menú de la app
    menu ='''
        A. Listar con nombre y posición a todos los jugadores del Dream Team
        B. Seleccionar un jugador por su índice
        C. Buscar jugador por nombre y mostrar sus logros
        D. Mostrar promedio de puntos por partido del equipo
        E. Mostrar jugadores del salón de la fama
        F. Jugador con mas rebotes
        G. Promedio de asistencias por partido de cada jugador
        H. Guardar promedio asistencias en archivo CSV
        I. Guardar promedio asistencias en archivo JSON
        J. Guardar en la base de datos cada promedio de asistencias
        k. Listar nombre de forma descendente segun suma de robos y bloqueos
        L. Listar nombre y porcentaje de forma descendente segun suma de robos y bloqueos
        M. Indicar cantidad a listar de forma descendente segun suma de robos y bloqueos
        N. Crear tabla en base de datos con las posiciones
        0. Salir	
        '''
    imprimir_dato(menu)
    
def nba_menu_principal():
    imprimir_menu()
    return pedir_opcion()

def limpiar_consola() -> None:
    _ = input("\n Presione una tecla para continuar")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

def pedir_opcion():
    opcion = input("Por favor elija una opción: ")
        #opcion = int(opcion) if validar_entero(opcion) else -1
    return opcion.upper()

def obtener_nombre_y_posicion(jugador:object):
    nombre = jugador.nombre
    posicion = jugador.posicion
    return f"{nombre} - {posicion}"

def nba_imprimir_nombre_y_posicion(lista_jugadores:list[object]):
    for jugador in lista_jugadores:
        mensaje = obtener_nombre_y_posicion(jugador)
        imprimir_dato(mensaje)

def pedir_jugador():
    jugador_elegido = input("Ingrese el índce de jugador: ")
    jugador_elegido = validar_indice(jugador_elegido)
    return int(jugador_elegido)
    
def validar_indice(indice: int):
    validar_numero = "^([1-9]|1[0-2])$"
    while not re.match(validar_numero,indice):
        indice = input("El equipo tiene solo 12 jugadores, ingrese un índce correcto: ")
    return indice

def buscar_jugador_en_lista(lista_jugadores:list[object], indice_jugador:int):
    indice_jugador -= 1
    jugador = lista_jugadores[indice_jugador]
    return jugador

def obtener_datos_jugador_elegido(jugador:object):
    jugador_elegido = {
        "nombre":jugador.nombre,
        "Posicion":jugador.posicion,
        "temporadas":jugador.estadisticas.temporadas,
        "puntos":jugador.estadisticas.puntos_totales,
        "promedio_puntos":jugador.estadisticas.promedio_puntos_por_partido,
        "rebotes": jugador.estadisticas.rebotes_totales,
        "promedio_rebotes": jugador.estadisticas.promedio_rebotes_por_partido,
        "asistencias": jugador.estadisticas.asistencias_totales,
        "promedio_asistencias": jugador.estadisticas.promedio_asistencias_por_partido,
        "robos": jugador.estadisticas.robos_totales,
        "bloqueos": jugador.estadisticas.bloqueos_totales,
        "porcentaje_tiros_de_campo": jugador.estadisticas.porcentaje_tiros_de_campo,
        "porcentaje_de_tiros_libres":jugador.estadisticas.porcentaje_tiros_libres,
        "porcentaje_de_tiros_triples":jugador.estadisticas.porcentaje_tiros_triples
    }
    return jugador_elegido
    
def nba_imprimir_estadisticas_jugador_elegido(jugador:object):
    mensaje = f'''
    Estadísticas de {jugador.nombre}
    Temporadas jugadas: {jugador.estadisticas.temporadas}
    Puntos totales: {jugador.estadisticas.puntos_totales}
    Promedio de puntos por partido: {jugador.estadisticas.promedio_puntos_por_partido}
    Rebotes: {jugador.estadisticas.rebotes_totales}
    Promedio de rebotes: {jugador.estadisticas.promedio_rebotes_por_partido}
    Asistencias realizadas: {jugador.estadisticas.asistencias_totales}
    Promedio de asistencias: {jugador.estadisticas.promedio_asistencias_por_partido}
    Robos realizados: {jugador.estadisticas.robos_totales}
    Bloqueos: {jugador.estadisticas.bloqueos_totales}
    Porcentaje de tiros de campo: {jugador.estadisticas.porcentaje_tiros_de_campo}
    Porcentaje de tiros libres: {jugador.estadisticas.porcentaje_tiros_libres}
    Porcentaje de triples: {jugador.estadisticas.porcentaje_tiros_triples}
            '''
    imprimir_dato(mensaje)

def optimizar_nombre(nombre:str):
    nombre = nombre.replace(" ","_")
    return nombre

def pedir_desicion():
    desicion = input("¿Desea guardar las estadísticas?\nIngrese si o no: ")
    while desicion.lower() != "si" and desicion.lower() != "no":
        desicion = input("¿Desea guardar las estadísticas?\nIngrese si o no: ")
    return desicion.lower()

def guardar_estadisticas_jugador(ruta:str,jugador:dict, desicion:str, nombre:str="Uribarri"):
    if  desicion == "si":
        try:
            nombre = optimizar_nombre(nombre)
            ruta += f"{nombre}.csv"
            equipo.crear_csv(ruta,jugador)
        except Exception as ex:
           print(f"No fue posible guardar el archivo {str(ex)} {ruta}")
    else:
        print("No se guardarán las estadisticas")

def validar_nombre(nombre:str):
    regex = "^[a-zA-Z]+( [a-zA-Z]+)?"
    while not re.match(regex, nombre):
        nombre = input("El nombre ingresado no es válido, ingrese otro: ")
    return nombre
    
def buscar_jugador(lista_jugadores:list[object])->dict:
    nombre = validar_nombre(input("Ingrese el nombre del jugador: "))
    for jugador in lista_jugadores:
        if jugador.nombre.lower() == nombre.lower():
           return jugador
    return None
                  
def nba_imprimir_logros(jugador:object):
    mensaje = "El jugador ingresado no es parte del equipo"
    if jugador is not None:
        mensaje = f"{jugador.nombre}\n"
        for logro in jugador.logros:
            mensaje += f"> {logro}\n"
    imprimir_dato(mensaje)

def obtener_lista_promedio_puntos_jugador(lista_jugadores:list[object]):
    #Recibe una lista de jugadores(objectos)
    #Obtiene el promedio de puntos de cada uno de ellos 
    #Retorna una lista con cada promedio de puntos
    lista_puntos = [jugador.estadisticas.promedio_puntos_por_partido for jugador in lista_jugadores]
    return lista_puntos

def acumular_puntos(lista_jugadores:list[object]):
    #Recibe una lista de jugadores(objetos)
    #Suma todos los valores
    #Retorna la suma
    lista_puntos = obtener_lista_promedio_puntos_jugador(lista_jugadores)
    acumulador = sum(lista_puntos)
    return acumulador

def calcular_promedio_puntos(lista_jugadores:list[object]):
    #Retorna el primedio de puntos por partido del equipo
    puntos = acumular_puntos(lista_jugadores)
    cantidad_jugadores = len(lista_jugadores)

    promedio = 0
    try:
        promedio = puntos / cantidad_jugadores
    except ZeroDivisionError:
        print("No es posible dividir por cero")

    return round(promedio,2)

def ordenar_lista(lista:list[int]):
    #Recibe una lista de enteros
    #La ordena de manera ascendente
    #Retorna la lista ordenada
    if len(lista) < 2:
        return lista
    
    pivot = lista.pop()
    mas_grandes = []
    mas_chicos = []
    for numero in lista:
        if numero > pivot:
            mas_grandes.append(numero)
        elif numero <= pivot:
            mas_chicos.append(numero)
    return ordenar_lista(mas_chicos) + [pivot] + ordenar_lista(mas_grandes)

def ordenar_indices_jugadores_por_promedio_puntos(lista_jugadores:list[object]):
    lista_indices_jugadores = []
    lista_puntos = obtener_lista_promedio_puntos_jugador(lista_jugadores)
    copia_lista_puntos = deepcopy(lista_puntos)
    lista_puntos_ordenada = ordenar_lista(lista_puntos)
    for item in lista_puntos_ordenada:
        lista_indices_jugadores.append(copia_lista_puntos.index(item))
    
    return lista_indices_jugadores

def nombres_ordenados_por_promedio_puntos(lista_jugadores:list[object]):
    indices = ordenar_indices_jugadores_por_promedio_puntos(lista_jugadores)
    jugadores_ordenados_ascendente = []
    for item in indices:
        jugadores_ordenados_ascendente.append(lista_jugadores[item])
    return jugadores_ordenados_ascendente

def nba_imprimir_promedio_puntos_y_jugadores(promedio_total:float,lista_jugadores:list[object]):
    mensaje = "Promedio personal de puntos por partido:\n"
    for jugador in lista_jugadores:
        mensaje += f"{jugador.nombre}: {jugador.estadisticas.promedio_puntos_por_partido}\n"
    mensaje += f"El promedio de puntos por partido del Dream Team es: {promedio_total} puntos\n"
    imprimir_dato(mensaje)

def normalizar_expresion(expresion:str):
    expresion = f"{expresion.replace('^','').replace('$','')}"
    return expresion

def evaluar_si_es_miembro_salon_fama(jugador:object)->bool:
    mensaje = ""
    expresion = "^Miembro del Salon de la Fama del Baloncesto$"
    flag = False
    if jugador is not None:
        mensaje += f"{jugador.nombre}\n"
        flag = [True for item in jugador.logros if re.match(expresion,item)]     
    if flag:
        mensaje += normalizar_expresion(expresion)
    else:
        mensaje += "No pertenece al Salón de la Fama"
    return mensaje
        
def nba_imprimir_si_es_miembro_o_no(mensaje:str):
    imprimir_dato(mensaje)
    
def calcular_indice_jugador_mas_rebotes(lista_jugadores:list[object]):
    lista_rebotes = []
    for jugador in lista_jugadores:
        lista_rebotes.append(jugador.estadisticas.rebotes_totales)  
    copia_lista_rebotes = deepcopy(lista_rebotes)
    lista_rebotes_ordenada = ordenar_lista(lista_rebotes)
    indice_del_jugador = copia_lista_rebotes.index(lista_rebotes_ordenada.pop())
    return lista_jugadores[indice_del_jugador]

def obtener_nombre_y_rebotes(jugador:object):
    mensaje = f"El jugador con más rebotes es {jugador.nombre} con {jugador.estadisticas.rebotes_totales}"
    return mensaje

def nba_imprimir_nombre_jugador_mas_rebotes(mensaje:str):
    imprimir_dato(mensaje)


def quick_sort(lista_jugadores:list[object]):
    #Recibe una lista de enteros
    #La ordena de manera ascendente
    #Retorna la lista ordenada
    if len(lista_jugadores) < 2:
        return lista_jugadores
    
    jugador = lista_jugadores.pop()
    pivot = jugador.estadisticas.promedio_asistencias_por_partido
    mas_grandes = []
    mas_chicos = []
    iguales = [jugador]
    for jugador in lista_jugadores:
        if jugador.estadisticas.promedio_asistencias_por_partido > pivot:
            mas_grandes.append(jugador)
        elif jugador.estadisticas.promedio_asistencias_por_partido < pivot:
            mas_chicos.append(jugador)
        else:
            iguales.append(jugador)
    return quick_sort(mas_grandes) + iguales + quick_sort(mas_chicos)

def nba_imprimir_promedio_asistencias_y_jugadores(lista_jugadores:list[object]):
    lista_ordenada_asistencias = quick_sort(lista_jugadores)
    for jugador in lista_ordenada_asistencias:
        imprimir_dato(f"{jugador.nombre} {jugador.estadisticas.promedio_asistencias_por_partido}")


def crear_datos_promedio_asistencias_partido(lista_jugadores:list[object]):
    lista_jugadores_ordenada = quick_sort(lista_jugadores)
    jugador_diccionario = []
    for jugador in lista_jugadores_ordenada:
        jugador_diccionario.append({jugador.nombre : jugador.estadisticas.promedio_asistencias_por_partido})
        
    return jugador_diccionario

def nba_guardar_promedio_asistencias_db(ruta,jugadores:list[dict]):
    sentencia = """create table if not exists promedio_asistencias_jugadores
                            (id integer primary key autoincrement,
                            nombre text,
                            promedio_asistencias real)"""
    equipo.eliminar_tabla_base_datos(ruta, "promedio_asistencias_jugadores")
    equipo.crear_tabla_base_datos(ruta, sentencia)
    equipo.agregar_a_base_datos(ruta, jugadores)

def validar_nombre_archivo(nombre_ruta:str):
    regex = r"^\w+\S*(-_\.)*\w$"
    return True if re.match(regex,nombre_ruta) else False

def pedir_nombre_ruta():
    nombre_ruta = input("Ingrese del archivo: ")
    while not validar_nombre_archivo(nombre_ruta):
        nombre_ruta = input("Nombre incorrecto,caracteres especiales permitidos(. _ -)\nNo puede comenzar ó terminar con caracteres especiales\nIntente nuevamente: ")
    return nombre_ruta

def armar_ruta_json(path:str,nombre_archivo:str):
    ruta = path + nombre_archivo + ".json"
    return ruta

def nba_crear_archivo_json(ruta:str, lista_jugadores:list[dict]):
    equipo.crear_json(ruta,lista_jugadores)

def ordenar_robos_mas_bloqueos(lista_jugadores: list[object]):
    if not lista_jugadores:
        print("La lista está vacía")
    else:
        lista_copia = lista_jugadores.copy()
        lista_copia.sort(key=lambda jugador: jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales, reverse=True)
        return lista_copia
    
def mostrar_cantidad_jugadores():
    cantidad = input("¿Cuántos jugadores desea mostrar?: ")
    validar_indice(cantidad)
    return cantidad   

def calcular_porcentaje(jugador:object,maximo):
    suma = jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales
    porcentaje = (suma*100)/maximo
    return round(porcentaje,2)

def nba_listar_por_robos_mas_bloqueos(lista_jugadores:list[object],con_datos:bool=False,cantidad:bool=False):
    lista_ordenada = ordenar_robos_mas_bloqueos(lista_jugadores)
    if cantidad and not con_datos:
        numero_ingresado = int(mostrar_cantidad_jugadores())
        lista_cortada =  lista_ordenada[:numero_ingresado]
        for jugador in lista_cortada:
            imprimir_dato(jugador.nombre)
    elif con_datos and not cantidad:
        for jugador in lista_ordenada:
            maximo = lista_ordenada[0].estadisticas.robos_totales + lista_ordenada[0].estadisticas.bloqueos_totales
            imprimir_dato(f"{jugador.nombre} {calcular_porcentaje(jugador,maximo)} %")
    elif not con_datos and not cantidad:
        for jugador in lista_ordenada:
            imprimir_dato(f"{jugador.nombre} {jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales}")

def obtener_posiciones(lista_jugadores:list[object]):
    lista_posiciones=[]
    for jugador in lista_jugadores:
        if not jugador.posicion in lista_posiciones:
            lista_posiciones.append(jugador.posicion)

    return lista_posiciones

def nba_crear_posiciones(ruta,lista_posiciones:list):
    sentencia ="""create table if not exists posiciones (id integer primary key autoincrement, 
                                                        posicion text)"""
    equipo.eliminar_tabla_base_datos(ruta,"posiciones")
    equipo.crear_tabla_base_datos(ruta,sentencia)
    equipo.agregar_posiciones_a_tabla(ruta,lista_posiciones)

