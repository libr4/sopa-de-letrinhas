from pyglet.gl import *
from partida import Partida
from estados import Estados
from __init__ import *

class Tela_jogo():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.btn_enviar = Btn_Enviar(300, 50, 200, 70)
        self.btn_deletar = Btn_Deletar(900, 50, 200, 70)
        self.pt = Partida()
        self.partida = self.pt.gerar_partida()
        self.letras_embaralhadas = self.partida["letras_embaralhadas"]
        self.classe_letras_embaralhadas = []
        self.campo_resposta = Campo_resposta(400, 160, 300, 70)
        self.area_resp_certas = Area_respostas_certas(100, 240, 1150, 320)
        self.palavras_certas = self.partida["palavras"]
        self.gera_letras_embaralhadas()

        self.componentes_clicaveis = [self.btn_enviar, self.btn_deletar, *self.classe_letras_embaralhadas]

    def gera_letras_embaralhadas(self):
        pos = 0
        letra_distancia = 70
        for caractere in self.letras_embaralhadas:
            self.classe_letras_embaralhadas.append(Letra(480 + pos, 110, letra_distancia, letra_distancia, caractere)) #transforma
            pos += letra_distancia

    def draw(self):
        self.btn_enviar.draw()
        self.btn_deletar.draw()
        self.area_resp_certas.draw()
        self.campo_resposta.draw()
        for letra in self.classe_letras_embaralhadas:
            letra.draw()
