from typing import Tuple
import pyglet
from abc import ABC, abstractmethod

class Widget(ABC):
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contem_ponto(self, x, y):
        return x >= self.x and x <= self.x + self.width \
            and y >= self.y and y <= self.y + self.height

    @abstractmethod
    def draw(self):
        pass

    @classmethod
    def gerar_label(cls, x:int, y:int, width:int, height:int, texto:str = "", color:Tuple = (0, 0, 0, 255), **kwargs):
        label = pyglet.text.Label(texto,
                font_name='askhjflk',
                font_size=kwargs['font_size'] if 'font_size' in kwargs else 32,
                color=color,
                anchor_x=kwargs['anchor_x'] if 'anchor_x' in kwargs else 'center', 
                anchor_y=kwargs['anchor_y'] if 'anchor_y' in kwargs else 'center',
                x = x + width // 2,
                y = y + height // 2)
        return label
