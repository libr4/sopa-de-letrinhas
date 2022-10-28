import pyglet
from Widgets import Botao

class Tela_Inicial:
    def __init__(self):
        self.iniciar = Btn_Iniciar(300, 50, 200, 70)
        self.high_scores = Btn_High_Scores(900, 50, 200, 70)
        self.sair = Btn_Sair(500, 50, 200, 70)
    def draw(self):
        self.iniciar.draw()
        self.high_scores.draw()
        self.sair.draw()

class Btn_Iniciar(Botao):
    def __init__(self, x, y, width, height, texto="Iniciar"):
        super().__init__(x, y, width, height, texto)
    def click(self):
        pass
class Btn_High_Scores(Botao):
    def __init__(self, x, y, width, height, texto="Ranking"):
        super().__init__(x, y, width, height, texto)
    def click(self):
        pass
class Btn_Sair(Botao):
    def __init__(self, x, y, width, height, texto="Sair"):
        super().__init__(x, y, width, height, texto)
    def click(self):
        pass
    # def draw(self):

