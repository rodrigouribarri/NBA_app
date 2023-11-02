import json, sqlite3
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


    def crear_encabezado(self,jugador:dict):
        texto = ""
        for clave in jugador.keys():
            texto += f"{clave}, "
        texto += "\n"
        return texto
    
    def crear_datos(self,jugador:dict):
        texto = ""
        for valor in jugador.values():
            texto += f"{valor}, "
            
        texto += "\n"
        return texto
    
    def crear_json(self, ruta: str, lista_jugadores: list[dict]) -> None:
        with open(ruta, "w", encoding="utf-8") as archivo_json:
            contenido = [{"promedio_asistencias": lista_jugadores}]           
            json.dump(contenido, archivo_json, indent=4)
            print(f'Archivo creado en la ruta: {ruta}')

    

    def eliminar_tabla_base_datos(self, ruta):
        with sqlite3.connect(ruta) as conexion:
            try:
                conexion.execute("drop table if exists promedio_asistencias_jugadores ")
                conexion.commit()
            except Exception as ex:
                print("No fue posible eliminar la tabla")
    
    def crear_tabla_base_datos(self, ruta):
        with sqlite3.connect(ruta) as conexion:
            try:
                sentencia = """create table if not exists promedio_asistencias_jugadores
                            (id integer primary key autoincrement,
                            nombre text,
                            promedio_asistencias real)"""
                conexion.execute(sentencia)
                conexion.commit()
            except Exception as ex:
                print("No fue posible crear la tabla")

    def agregar_a_base_datos(self, ruta, jugadores:list[dict]):
        with sqlite3.connect(ruta) as conexion:
            try:
                for jugador in jugadores:
                    for clave, valor in jugador.items():
                        conexion.execute("insert into promedio_asistencias_jugadores(nombre, promedio_asistencias) values (?,?)",(clave, valor))
                conexion.commit()
                print("Datos agregados exitosamente")
            except Exception as ex:
                print(f"No fue posible agregar los datos {str(ex)}")

                
   






