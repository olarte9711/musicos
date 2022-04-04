from random import randint
from secrets import choice
from logica.bandola import Bandola
from logica.instrumento import Instrumento
from logica.guitarra import Guitarra
from logica.bajo import Bajo
from logica.triple import Triple
from logica.bandola import Bandola
from logica.afinador import Afinador
from logica.musico import Musico
from random import randint, choice

class Banda():
    def __init__(self):
        self.musicos = []
    
    def crear_banda(self):
        for i in range(randint(1,5)):
            self.musicos.append(Musico())
        
        for i in self.musicos:
            i.asignar_instrumento(self.generar_instrumento())

    def afinar(self):
        for musico in self.musicos:
            afinador = Afinador(musico)
            afinador.afinar()

    def tocar(self):
        for musico in self.musicos:
            musico.tocar()
    
    def generar_instrumento(self):
        instrumentos = [Guitarra(), Bajo(), Triple(), Bandola()]
        return choice(instrumentos)
