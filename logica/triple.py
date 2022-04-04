from logica.instrumento import Instrumento

class Triple(Instrumento):
    def tocar(self):
        print("Tocando triple")
    def afinar(self):
        print("Afinando triple")