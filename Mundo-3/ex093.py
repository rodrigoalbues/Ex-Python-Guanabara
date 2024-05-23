"""Crie um prog que gerencie o aproveitamento de um jogador de futebol. O prog vai ler o nome dele e qts partidas ele jogou. Depois vai ler a qtd de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

print("=" * 60)
nome = input("Nome do jogador: ")
partidas = input(f"Quantas partidas {nome} jogou? ")
jogador = {"nome": nome}
gols_partida = []
if partidas.isdigit():
    partidas = int(partidas)
    for p in range(partidas):
        gols = input(f"Quantos gols na {p+1}ª partida? ")
        if gols.isdigit():
            gols = int(gols)
            gols_partida.append(gols)

        else:
            print("Informação inválida! Por favor, insira um número válido de gols.")
            break
    tot_gols = sum(gols_partida)
    jogador.update(
        {
            "gols": gols_partida,
            "total": tot_gols,
        }  # type: ignore
    )  # type: ignore
    print("-" * 60)
    print(jogador)
    print("-" * 60)
    for k, v in jogador.items():
        print(f"O campo {k} tem o valor {v}.")
    print("-" * 60)
    print(f"O jogador {nome} jogou {partidas} partidas.")
    for p, g in enumerate(gols_partida):
        print(f"    => Na parida {p + 1}, fez {g} gols.")
    print(f"Fez um total de {tot_gols} gols.")
else:
    print("Informação inválida!")
print("=" * 60)
