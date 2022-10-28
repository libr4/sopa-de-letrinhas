from pyglet.gl import *
from partida import Partida
from estados import Estados
from __init__ import *
from Views.Tela_jogo import Tela_jogo
# from Views.Tela_Inicial import Tela_Inicial

class Janela(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.state = Estados.JOGO
        # self.menu = Tela_Inicial()

        self.jogo = Tela_jogo()
        self.letras_embaralhadas = self.jogo.partida["letras_embaralhadas"]
        self.classe_letras_embaralhadas = self.jogo.classe_letras_embaralhadas
        self.palavras_certas = self.jogo.partida["palavras"]
        self.componentes_clicaveis = self.jogo.componentes_clicaveis
        self.campo_resposta = self.jogo.campo_resposta
        self.area_resp_certas = self.jogo.area_resp_certas
        
        k = pyglet.image.load("background.png")
        print(k.anchor_x, k.anchor_y)
        k.anchor_x = 50
        k.anchor_y = -20
        self.sprite =pyglet.sprite.Sprite(k)

    def troca_componentes(self):
        pass
        
    def on_draw(self):
        window.clear()

        self.sprite.draw()
        match self.state:
            case Estados.MENU:
                self.menu.draw()
            case Estados.JOGO:
                self.jogo.draw()
            case _: #default
                print("default")

    # def on_key_press(self, symbol, modifiers):
    #     letra = chr(symbol)
    #     if letra in self.letras_embaralhadas:
    #         self.campo_resposta.digita(letra)
    #     elif symbol == pyglet.window.key.BACKSPACE:
    #         self.campo_resposta.deleta()
    #     elif symbol == pyglet.window.key.ENTER:
    #         self.btn_enviar.click(self.campo_resposta, self.palavras_certas, self.area_resp_certas)

    def on_mouse_press(self, x, y, button, modifiers):
        for componente in self.componentes_clicaveis:
            if componente.contem_ponto(x, y):
                componente.click(self.campo_resposta, self.palavras_certas, self.area_resp_certas)

window = Janela(1280, 720)
# glClearColor(0.3, 0.88, 0.9, 1.0)
glClearColor(1, 1, 1, 1.0)
window.maximize()
pyglet.app.run()