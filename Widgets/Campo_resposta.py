from .widgets import Widget

class Campo_resposta(Widget):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        self.label = Widget.gerar_label(x, y, width, height, anchor_x = 'left', anchor_y = 'baseline')

    def draw(self):
        self.label.draw()
    def digita(self, letra):
        self.label.text += str(letra)
    def deleta(self):
        self.label.text = self.label.text[0:-1]