from pyglet.gl import *
from partida import Partida
from estados import Estados
from __init__ import *
from Views.Tela_jogo import Tela_jogo
from Views.Tela_Inicial import Tela_Inicial

class Janela(pyglet.window.Window):
    state:Estados = Estados.MENU
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.menu = Tela_Inicial()
        self.jogo = Tela_jogo()

        self.letras_embaralhadas = self.jogo.partida["letras_embaralhadas"]
        self.classe_letras_embaralhadas = self.jogo.classe_letras_embaralhadas
        self.palavras_certas = self.jogo.partida["palavras"]

        self.campo_resposta = self.jogo.campo_resposta
        self.area_resp_certas = self.jogo.area_resp_certas

        self.argumentos = [Janela.troca_estado, pyglet.app.exit]
        self.componentes_clicaveis = self.menu.componentes_clicaveis
        
        background = pyglet.image.load("Assets/background.png")
        print(background.anchor_x, background.anchor_y)
        background.anchor_x = 50
        # background.anchor_y = -20
        self.sprite = pyglet.sprite.Sprite(background)

    @classmethod
    def troca_estado(cls, state):
        cls.state = state

    def troca_componentes(self):
        pass

    def tela_jogo(self):
        self.componentes_clicaveis = self.jogo.componentes_clicaveis
        self.argumentos = [self.campo_resposta, self.palavras_certas, self.area_resp_certas, self.state]

    def on_draw(self):
        window.clear()

        self.sprite.draw()

        match Janela.state:
            case Estados.JOGO:
                self.tela_jogo()
                self.jogo.draw()
            case _: #default
                self.menu.draw()
                print("default")

    def on_key_press(self, symbol, modifiers):
        if Janela.state == Estados.JOGO:
            letra = chr(symbol)
            if letra in self.letras_embaralhadas:
                self.campo_resposta.digita(letra)
            elif symbol == pyglet.window.key.BACKSPACE:
                self.campo_resposta.deleta()
            elif symbol == pyglet.window.key.ENTER:
                btn_enviar = self.componentes_clicaveis[0]
                btn_enviar.click(self.campo_resposta, self.palavras_certas, self.area_resp_certas)

    def on_mouse_press(self, x, y, button, modifiers):
        for componente in self.componentes_clicaveis:
            if componente.contem_ponto(x, y):
                componente.click(*self.argumentos)

window = Janela(1280, 720)
# glClearColor(0.3, 0.88, 0.9, 1.0)
glClearColor(1, 1, 1, 1.0)
window.maximize()
pyglet.app.run()