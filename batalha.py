def atacar(atacante, defensor, indice_atacante, indice_defensor):
    carta_atacante = atacante.campo[indice_atacante]
    carta_defensora = defensor.campo[indice_defensor]

    print(f"\n{atacante.nome} atacou com {carta_atacante.nome}!")

    carta_defensora.defesa -= carta_atacante.ataque
    carta_atacante.defesa -= carta_defensora.ataque

    print(
        f"{carta_defensora.nome} recebeu "
        f"{carta_atacante.ataque} de dano."
    )

    print(
        f"{carta_atacante.nome} recebeu "
        f"{carta_defensora.ataque} de dano."
    )

    if not carta_defensora.esta_viva():
        print(f"{carta_defensora.nome} foi derrotada!")

    if not carta_atacante.esta_viva():
        print(f"{carta_atacante.nome} foi derrotada!")

    atacante.remover_cartas_derrotadas()
    defensor.remover_cartas_derrotadas()


def ataque_direto(atacante, defensor, indice_atacante):
    carta = atacante.campo[indice_atacante]

    defensor.vida -= carta.ataque

    if defensor.vida < 0:
        defensor.vida = 0

    print(
        f"\n{carta.nome} atacou diretamente "
        f"{defensor.nome} causando {carta.ataque} de dano!"
    )