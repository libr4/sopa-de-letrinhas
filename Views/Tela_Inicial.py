import pyglet
from estados import Estados
from Widgets.Botao import Botao
# from main import Janela <- isso da prob de circular import

class Tela_Inicial:
    def __init__(self):
        self.iniciar = Btn_Iniciar(580, 450, 200, 70)
        self.high_scores = Btn_High_Scores(580, 350, 200, 70)
        self.sair = Btn_Sair(580, 250, 200, 70)
        self.componentes_clicaveis = [self.iniciar, self.high_scores, self.sair]
    def draw(self):
        self.iniciar.draw()
        self.high_scores.draw()
        self.sair.draw()

class Btn_Iniciar(Botao):
    def __init__(self, x, y, width, height, texto="Iniciar"):
        super().__init__(x, y, width, height, texto)
    def click(self, *argumentos): #o proprio metodo da classe eh passado, isso burla o prob de circular import, pois importar a classe torna-se desnecessario
        change_state = argumentos[0]
        change_state(Estados.JOGO)
        # print("state", state)
class Btn_High_Scores(Botao):
    def __init__(self, x, y, width, height, texto="Ranking"):
        super().__init__(x, y, width, height, texto)
    def click(self):
        pass
class Btn_Sair(Botao):
    def __init__(self, x, y, width, height, texto="Sair"):
        super().__init__(x, y, width, height, texto)
    def click(self, *argumentos):
        fechar = argumentos[1]
        fechar()
    # def draw(self):

