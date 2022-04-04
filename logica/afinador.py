from logica.instrumento import Instrumento

class Afinador():
    def __init__(self, musico):
        self.musico = musico
        self.instrumento = musico.instrumento

    def afinar(self):
        self.instrumento.afinar()
    
    def tocar(self):
        self.instrumento.tocar()