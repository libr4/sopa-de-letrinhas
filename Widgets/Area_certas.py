import pyglet
from .widgets import Widget

class Area_respostas_certas(Widget):
    N_CAMPOS = 4
    DISTANCIA_CAMPOS = 320
    DISTANCIA_LINHAS = 40
    QTD_LINHAS = 8

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        self.moldura = pyglet.shapes.BorderedRectangle(self.x, self.y + 50, self.width, self.height, border=5, color=(255, 255, 255), border_color=(0,0,0))
        self.colunas = [[], [], [], []]
        self.texto_interno()

    def texto_interno(self):
        pos_horizontal = 0
        for coluna in range(Area_respostas_certas.N_CAMPOS):
            texto = str(3 + coluna) + " letras" #se for a primeira linha de kd coluna, mostra "n letras" se nao, fica em branco ate receber uma resposta certa
            pos_vertical = 0
            tamanho = 32
            for linha in range(Area_respostas_certas.QTD_LINHAS):
                self.colunas[coluna].append(Widget.gerar_label(
                            self.x - 50 + pos_horizontal, 
                            self.y + 300 - pos_vertical, 
                            300, 70, 
                            texto,
                            font_size=tamanho
                            ))
                texto = ""
                tamanho = 24
                pos_vertical += 60 if linha == 0 else Area_respostas_certas.DISTANCIA_LINHAS
            pos_horizontal += Area_respostas_certas.DISTANCIA_CAMPOS

    def draw(self):
        self.moldura.draw()
        for coluna in self.colunas:
            for linha in range(Area_respostas_certas.QTD_LINHAS):
                coluna[linha].draw()

    def digita(self, coluna:int, palavra:str):
        for campo in self.colunas[coluna]:
            if campo.text == "":
                campo.text = palavra
                break