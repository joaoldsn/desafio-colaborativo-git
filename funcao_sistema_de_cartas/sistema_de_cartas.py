class Carta: # Cria uma classe chamada Carta. A classe funciona como um "molde" para criar cartas.
    def __init__(self, nome, ataque, defesa): #O __init__ é o método chamado automaticamente quando criamos uma nova Carta.
        self.nome = nome   # self = representa a própria carta que está sendo criada
        self.ataque = ataque
        self.defesa = defesa
