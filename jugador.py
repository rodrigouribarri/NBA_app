from estadistica import Estadistica
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = ""
        self.estadisticas = Estadistica()
        self.logros = []
    
    def jugador(self, jugador):
        return Jugador()
      
    @property
    def posicion(self):
        return self._posicion
    
    @posicion.setter
    def posicion(self, value):
        self._posicion = value

    
    