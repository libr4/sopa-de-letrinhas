import pyglet
from abc import ABC, abstractmethod
from .widgets import Widget
# from ..main import *


class Botao(Widget, ABC):
    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height)
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,75,173), border_color=(255, 255, 255))
        self.label = Widget.gerar_label(self.x, self.y, self.width, self.height, self.texto, (255, 255, 255, 255))
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    @abstractmethod
    def click(self):
        pass


class Btn_Deletar(Botao):
    def __init__(self, x, y, width, height, texto="deletar"):
        super().__init__(x, y, width, height, texto)
    def click(self, campo_resposta, palavras_certas, area_resp_certas):
        campo_resposta.deleta()


class Btn_Enviar(Botao):
    def __init__(self, x, y, width, height, texto="enviar"):
        super().__init__(x, y, width, height, texto)

    def click(self, campo_resposta, palavras_certas:list[ str ], area_resp_certas):
        palavra = campo_resposta.label.text
        print(palavra, palavras_certas)
        if palavra in palavras_certas:
            campo_resposta.label.text = ""

            note = pyglet.resource.media("acerto.wav")
            note.play()

            coluna = len(palavra) - 3 #palavra eh, aqui, a resposta certa dada pelo jogador
            area_resp_certas.digita(coluna, palavra)
            palavras_certas.remove(palavra)