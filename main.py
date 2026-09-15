from carta import Carta
from jogador import Jogador
from batalha import atacar, ataque_direto


def criar_baralho(jogador):
    cartas = [
        Carta("Dragão de Fogo", 7, 5),
        Carta("Cavaleiro de Prata", 4, 6),
        Carta("Goblin Guerreiro", 3, 2),
        Carta("Gigante da Montanha", 6, 7)
    ]

    for carta in cartas:
        jogador.adicionar_carta(carta)


def escolher_carta(jogador):
    jogador.mostrar_campo()

    while True:
        try:
            escolha = int(input("Escolha uma carta: ")) - 1

            if 0 <= escolha < len(jogador.campo):
                return escolha

            print("Escolha inválida.")

        except ValueError:
            print("Digite um número válido.")


def batalha(jogador1, jogador2):
    turno = jogador1

    while jogador1.vida > 0 and jogador2.vida > 0:

        print("\n" + "=" * 40)
        print(f"Turno de {turno.nome}")

        print(
            f"{jogador1.nome}: {jogador1.vida} PV | "
            f"{jogador2.nome}: {jogador2.vida} PV"
        )

        if not turno.campo:
            print(f"{turno.nome} não possui cartas.")
            break

        indice_atacante = escolher_carta(turno)

        outro = jogador2 if turno == jogador1 else jogador1

        print(f"\nCampo de {outro.nome}:")
        outro.mostrar_campo()

        if outro.campo:
            escolha = input(
                "\nDeseja atacar uma criatura? (s/n): "
            ).lower()

            if escolha == "s":
                indice_defensor = escolher_carta(outro)

                atacar(
                    turno,
                    outro,
                    indice_atacante,
                    indice_defensor
                )

            else:
                ataque_direto(
                    turno,
                    outro,
                    indice_atacante
                )

        else:
            ataque_direto(
                turno,
                outro,
                indice_atacante
            )

        turno = outro

    print("\n" + "=" * 40)

    if jogador1.vida <= 0:
        print(f"{jogador2.nome} venceu!")

    elif jogador2.vida <= 0:
        print(f"{jogador1.nome} venceu!")

    else:
        print("A batalha terminou!")


def main():
    print("=" * 40)
    print("      ⚔️ BATALHA DE CARTAS ⚔️")
    print("=" * 40)

    nome1 = input("Nome do Jogador 1: ")
    nome2 = input("Nome do Jogador 2: ")

    jogador1 = Jogador(nome1)
    jogador2 = Jogador(nome2)

    criar_baralho(jogador1)
    criar_baralho(jogador2)

    batalha(jogador1, jogador2)


if __name__ == "__main__":
    main()