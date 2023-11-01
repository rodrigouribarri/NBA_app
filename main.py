from desafio_nba import nba_app
from  equipo import Equipo

equipo = Equipo()
equipo.leer_json('./datos/dream_team.json')

if __name__ == '__main__':
    nba_app(equipo.lista_jugadores)