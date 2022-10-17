import random
# import pyglet

class Partida:
    def __init__(self, n):
        pass
    @classmethod
    def gerar_palavras(cls) -> list[str]:
        '''Retorna a lista de palavras que deverao ser descobertas pelo jogador'''
        file = open("partida.txt")
        partidas = file.readlines()
        tamanho = len(partidas) - 1
        linha = random.randint(0, tamanho)
        palavras_str = partidas[linha]
        palavras = palavras_str.split(",")
        return palavras
    @classmethod
    def gerar_letras(cls, palavras:str) -> list[str]:
        '''Recebe uma lista de palavras e retorna as seis letras para forma-las'''
        palavra_seis_letras = palavras[0]
        lista_seis_letras = [*palavra_seis_letras] #transforma a palavra de seis letras em uma lista de 6 letras
        random.shuffle(lista_seis_letras) #embaralha as letras
        return lista_seis_letras
    @classmethod
    def gerar_partida(cls) -> dict:
        '''Retorna uma lista de seis letras embaralhadas e as palavras formadas por ela e que o jogador devera descobrir'''
        palavras = Partida.gerar_palavras()
        letras_embaralhadas = Partida.gerar_letras(palavras)
        partida = {"letras_embaralhadas":letras_embaralhadas, "palavras":palavras}
        return partida
