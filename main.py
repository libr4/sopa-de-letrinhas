from pyglet.gl import *
from partida import Partida
import widgets

class Janela(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn_enviar = widgets.Btn_Enviar(300, 50, 200, 70)
        self.btn_deletar = widgets.Btn_Deletar(900, 50, 200, 70)
        self.partida = Partida.gerar_partida()
        self.letras_embaralhadas = self.partida["letras_embaralhadas"]
        self.classe_letras_embaralhadas = []
        self.campo_resposta = widgets.Campo_resposta(400, 230, 300, 70)
        self.area_resp_certas = widgets.Area_respostas_certas(30, 300, 1300, 420)
        self.palavras_certas = self.partida["palavras"]
        self.gera_letras_embaralhadas()

        self.componentes_clicaveis = [self.btn_enviar, self.btn_deletar, self.classe_letras_embaralhadas]

    def gera_letras_embaralhadas(self):
        pos = 0
        letra_distancia = 70
        for caractere in self.letras_embaralhadas:
            self.classe_letras_embaralhadas.append(widgets.Letra(480 + pos, 170, letra_distancia, letra_distancia, caractere)) #transforma
            pos += letra_distancia


    def on_draw(self):
        window.clear()
        self.btn_enviar.draw()
        self.btn_deletar.draw()
        self.campo_resposta.draw()
        self.area_resp_certas.draw()
        for letra in self.classe_letras_embaralhadas:
            letra.draw()

    def on_key_press(self, symbol, modifiers):
        letra = chr(symbol)
        if letra in self.letras_embaralhadas:
            self.campo_resposta.digita(letra)
        elif symbol == pyglet.window.key.BACKSPACE:
            self.campo_resposta.deleta()
        elif symbol == pyglet.window.key.ENTER:
            self.btn_enviar.click(self.campo_resposta, self.palavras_certas, self.area_resp_certas)
        

    def on_mouse_press(self, x, y, button, modifiers):
        for componente in self.componentes_clicaveis:
            if componente == self.classe_letras_embaralhadas:
                for letra in self.classe_letras_embaralhadas:
                    if letra.contem_ponto(x, y):
                        print(letra)
                        if letra.clicada == False: self.campo_resposta.digita(letra)
                        # letra.clicada = True
            elif componente == self.btn_deletar:
                if componente.contem_ponto(x, y):
                    self.campo_resposta.deleta()
            elif componente == self.btn_enviar:
                if componente.contem_ponto(x, y):
                    acertou = componente.click(self.campo_resposta, self.palavras_certas, self.area_resp_certas)
                    if acertou:
                        self.campo_resposta.label.text = ""
                        palavra = self.campo_resposta.label.text
                        note = pyglet.resource.media("acerto.wav")
                        note.play()
                        print(self.palavras_certas)
                        self.palavras_certas.remove(palavra)

window = Janela(1280, 720)
glClearColor(255, 255, 255, 255)
window.maximize()
pyglet.app.run()