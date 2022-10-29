# from widgets import Widget
import pyglet
from .widgets import Widget

class Letra(Widget):
    def __init__(self, x: int, y: int, width: int, height: int, letra:str):
        super().__init__(x, y, width, height)
        self.letra = letra
        self.label = pyglet.text.Label(self.letra,
                font_name='Arial',
                font_size=32,
                color=(0, 0, 0, 255),
                # anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
        self._clicada = False
    def draw(self):
        self.label.draw()
    def __repr__(self):
        return f"{self.letra}"
    def click(self, *argumentos):
        campo_resposta = argumentos[0]
        campo_resposta.digita(self.letra)
    @property
    def clicada(self):
        return self._clicada
    @clicada.setter
    def clicada(self, state):
        self._clicada = state