import json
from jugador import Jugador
from estadistica import Estadistica

class Equipo:
    def __init__(self) -> None:
        self.lista_jugadores = []
    
    @property
    def mostrar_lista_jugadores(self):
        return self.lista_jugadores
    
    def agregar_jugadores(self,jugador):
        self.lista_jugadores.append(jugador)
            
    def leer_json(self,ruta):
        try:
            with open(ruta,"r", encoding='utf-8') as archivo:
                dato = json.load(archivo)
                for jugador in dato["jugadores"]:
                    estad_a_cargar = jugador.get("estadisticas",{})
                    nuevo_jugador = Jugador(jugador.get("nombre","No tiene"))
                    nuevo_jugador.posicion = jugador.get("posicion","No tiene")
                    nuevo_jugador.estadisticas.temporadas_set = estad_a_cargar.get("temporadas")
                    nuevo_jugador.estadisticas.puntos_totales_set = estad_a_cargar.get("puntos_totales")
                    nuevo_jugador.estadisticas.promedio_puntos_por_partido_set = estad_a_cargar.get("promedio_puntos_por_partido")
                    nuevo_jugador.estadisticas.rebotes_totales_set = estad_a_cargar.get("rebotes_totales")
                    nuevo_jugador.estadisticas.promedio_rebotes_por_partido_set = estad_a_cargar.get("promedio_rebotes_por_partido")
                    nuevo_jugador.estadisticas.asistencias_totales_set = estad_a_cargar.get("asistencias_totales")
                    nuevo_jugador.estadisticas.promedio_asistencias_por_partido_set = estad_a_cargar.get("promedio_asistencias_por_partido")
                    nuevo_jugador.estadisticas.robos_totales_set = estad_a_cargar.get("robos_totales")
                    nuevo_jugador.estadisticas.bloqueos_totales_set = estad_a_cargar.get("bloqueos_totales")
                    nuevo_jugador.estadisticas.porcentaje_tiros_de_campo_set = estad_a_cargar.get("porcentaje_tiros_de_campo")
                    nuevo_jugador.estadisticas.porcentaje_tiros_libres_set = estad_a_cargar.get("porcentaje_tiros_libres")
                    nuevo_jugador.estadisticas.porcentaje_tiros_triples_set = estad_a_cargar.get("porcentaje_tiros_triples")
                    nuevo_jugador.logros = jugador.get("logros",[])
                    self.lista_jugadores.append(nuevo_jugador)          
        except Exception as ex:
           print(str(ex))


    # def crear_encabezado(self,jugador:dict):
    #     texto = ""
    #     for clave in jugador.keys():
    #         primer_dato = True
    #         if primer_dato:
    #             texto += f"{clave}"
    #             primer_dato = False
    #         else:
    #             texto += f", {clave}"
    #     texto += "\n"
    #     return texto
    
    def crear_datos(self,jugador:dict):
        texto = ""
        for valor in jugador.values():
            texto += f"{valor}, "
            
        auxiliar = (texto[:-1])
        auxiliar += "\n"
        return auxiliar
    
    def crear_csv(self, path:str,jugador:dict):
        #try:
            with open(path, "w") as archivo:
                texto = ""
                # texto += self.crear_encabezado(jugador)
                texto += self.crear_datos(jugador)
                archivo.write(texto)
                print("Archivo csv creado exitosamente")
                    
        #except Exception as ex:
        #    print(f"El archivo csv no se pudo crear {str(ex)}")
   






