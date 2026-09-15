class Carta: # Cria uma classe chamada Carta. A classe funciona como um "molde" para criar cartas.
    def __init__(self, nome, ataque, defesa): #O __init__ é o método chamado automaticamente quando criamos uma nova Carta.
        self.nome = nome   # self = representa a própria carta que está sendo criada
        self.ataque = ataque
        self.defesa = defesa

    def estar_viva(self): # Cria um método chamado esta_viva(), que serve para verificar se a carta ainda está viva.
        return self.defesa > 0   # Se a defesa for maior que 0, retorna True. Se a defesa for 0 ou menor, retorna False.
