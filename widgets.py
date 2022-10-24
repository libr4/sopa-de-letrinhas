from typing import Tuple
import pyglet

class Widget:
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contem_ponto(self, x, y):
        return x >= self.x and x <= self.x + self.width \
            and y >= self.y and y <= self.y + self.height

    def draw(self):
        pass
    @classmethod
    def gerar_label(cls, x:int, y:int, width:int, height:int, texto:str = "", color:Tuple = (0, 0, 0, 255), **kwargs):
        label = pyglet.text.Label(texto,
                font_name='Arial',
                font_size=kwargs['font_size'] if 'font_size' in kwargs else 32,
                color=color,
                anchor_x=kwargs['anchor_x'] if 'anchor_x' in kwargs else 'center', 
                anchor_y=kwargs['anchor_y'] if 'anchor_y' in kwargs else 'center',
                x = x + width // 2,
                y = y + height // 2)
        return label

class Botao(Widget):
    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height)
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,0,0), border_color=(255, 255, 255))
        self.label = Widget.gerar_label(self.x, self.y, self.width, self.height, self.texto, (255, 255, 255, 255))
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    def click(self):
        print("Clicou no botão")
    def __repr__(self):#isso nao faz nada
        return f"Botão '{self.texto}'"

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
    @property
    def clicada(self):
        return self._clicada
    @clicada.setter
    def clicada(self, state):
        self._clicada = state

class Campo_resposta(Widget):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        self.label = pyglet.text.Label("",
                font_name='Arial',
                font_size=32,
                # anchor_x='center', anchor_y='center',
                color=(0, 0, 0, 255),
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        self.label.draw()
    def digita(self, letra: Letra):
        self.label.text += str(letra)
    def deleta(self):
        self.label.text = self.label.text[0:-1]

class Btn_Deletar(Botao):
    def __init__(self, x, y, width, height, texto="deletar"):
        super().__init__(x, y, width, height, texto)
    def click(self, campo_resposta:Campo_resposta):
        campo_resposta.deleta()

class Area_respostas_certas(Widget):
    N_CAMPOS = 4
    DISTANCIA_CAMPOS = 320
    DISTANCIA_LINHAS = 70

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        self.moldura = pyglet.shapes.BorderedRectangle(self.x, self.y, self.width, self.height, border=5, color=(255, 255, 255), border_color=(0,0,0))
        self.colunas = [[], [], [], []]

        pos_horizontal = 0
        for coluna in range(Area_respostas_certas.N_CAMPOS):
            texto = str(3 + coluna) + " letras" #se for a primeira linha de kd coluna, mostra "n letras" se nao, fica em branco ate receber uma resposta certa
            pos_vertical = 0
            for linha in range(5):
                self.colunas[coluna].append(Widget.gerar_label(self.x - 50 + pos_horizontal, 
                            self.y + 350 - pos_vertical, 300, 70, 
                            texto,
                            ))
                texto = ""
                pos_vertical += Area_respostas_certas.DISTANCIA_LINHAS
            pos_horizontal += Area_respostas_certas.DISTANCIA_CAMPOS
    
    def draw(self):
        self.moldura.draw()
        for coluna in self.colunas:
            for linha in range(5):
                coluna[linha].draw()
    def digita(self, coluna:int, palavra:str):
        for campo in self.colunas[coluna]:
            if campo.text == "":
                campo.text = palavra
                break

class Btn_Enviar(Botao):
    def __init__(self, x, y, width, height, texto="enviar"):
        super().__init__(x, y, width, height, texto)
    
    def click(self, campo_resposta:Campo_resposta, palavras_certas:str, area_resp_certas:Area_respostas_certas):
        '''Retorna verdadeiro se o jogador acertou'''
        palavra = campo_resposta.label.text
        acertou = False
        if palavra in palavras_certas:
            acertou = True 
            coluna = len(palavra) - 3 #palavra eh, aqui, a resposta certa dada pelo jogador
            area_resp_certas.digita(coluna, palavra)
        return acertou #esse retorno serve para deletar a palavra na lista principal, para que o jogador nao mande a mesma palavra duas vezes