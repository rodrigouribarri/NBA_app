class Estadistica:
    def __init__(self) -> None:
        self._temporadas = 0
        self._puntos_totales = 0
        self._promedio_puntos_por_partido = 0
        self._rebotes_totales = 0
        self._promedio_rebotes_por_partido = 0
        self._asistencias_totales = 0
        self._promedio_asistencias_por_partido = 0
        self._robos_totales = 0
        self._bloqueos_totales = 0
        self._porcentaje_tiros_de_campo = 0
        self._porcentaje_tiros_libres = 0
        self._porcentaje_tiros_triples = 0

    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas_set(self, valor):
        self._temporadas = valor

    @property
    def puntos_totales(self):
        return self._puntos_totales
    
    @puntos_totales.setter
    def puntos_totales_set(self, valor):
        self._puntos_totales = valor

    @property
    def promedio_puntos_por_partido(self):
        return self._promedio_puntos_por_partido
    
    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido_set(self, valor):
        self._promedio_puntos_por_partido = valor

    @property
    def rebotes_totales(self):
        return self._rebotes_totales
    
    @rebotes_totales.setter
    def rebotes_totales_set(self, valor):
        self._rebotes_totales = valor

    @property
    def promedio_rebotes_por_partido(self):
        return self._promedio_rebotes_por_partido
    
    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido_set(self, valor):
        self._promedio_rebotes_por_partido = valor

    @property
    def asistencias_totales(self):
        return self._asistencias_totales
    
    @asistencias_totales.setter
    def asistencias_totales_set(self, valor):
        self._asistencias_totales = valor
    
    @property
    def promedio_asistencias_por_partido(self):
        return self._promedio_asistencias_por_partido
    
    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido_set(self, valor):
        self._promedio_asistencias_por_partido = valor

    @property
    def robos_totales(self):
        return self._robos_totales
    
    @robos_totales.setter
    def robos_totales_set(self, valor):
        self._robos_totales = valor

    @property
    def bloqueos_totales(self):
        return self._bloqueos_totales
    
    @bloqueos_totales.setter
    def bloqueos_totales_set(self, valor):
        self._bloqueos_totales = valor

    @property
    def porcentaje_tiros_de_campo(self):
        return self._porcentaje_tiros_de_campo 
    
    @porcentaje_tiros_de_campo.setter
    def porcentaje_tiros_de_campo_set(self, valor):
        self._porcentaje_tiros_de_campo = valor

    @property
    def porcentaje_tiros_libres(self):
        return self._porcentaje_tiros_libres 
    
    @porcentaje_tiros_libres.setter
    def porcentaje_tiros_libres_set(self, valor):
        self._porcentaje_tiros_libres = valor

    @property
    def porcentaje_tiros_triples (self):
        return self._porcentaje_tiros_triples 
    
    @porcentaje_tiros_triples.setter
    def porcentaje_tiros_triples_set(self, valor):
        self._porcentaje_tiros_triples = valor

    
