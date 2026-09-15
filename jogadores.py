class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 20
        self.campo = []

    def adicionar_carta(self, carta):
        self.campo.append(carta)

    def mostrar_campo(self):
        print(f"\nCampo de {self.nome}:")

        if not self.campo:
            print("Nenhuma carta no campo.")
            return

        for i, carta in enumerate(self.campo):
            print(f"{i + 1}. {carta}")

    def remover_cartas_derrotadas(self):
        self.campo = [
            carta for carta in self.campo
            if carta.esta_viva()
        ] ##a