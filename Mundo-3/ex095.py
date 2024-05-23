"""Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

jogadores = []
gols_partida = []
print("=" * 60)
while True:
    nome = input("Nome do jogador: ")
    partidas = input(f"Quantas partidas {nome} jogou? ")
    gols_partida.clear()
    jogador = {"nome": nome}
    if partidas.isdigit():
        partidas = int(partidas)
        for p in range(partidas):
            gols = input(f"Quantos gols na {p+1}ª partida? ")
            if gols.isdigit():
                gols = int(gols)
                gols_partida.append(gols)

            else:
                print(
                    "Informação inválida! Por favor, insira um número válido de gols."
                )
                break
        tot_gols = sum(gols_partida)
        jogador.update(
            {
                "gols": gols_partida[:],
                "total": tot_gols,
            }  # type: ignore
        )  # type: ignore
        jogadores.append(jogador)
        print()
        print("Jogador cadastrado com sucesso...")
        print("-" * 60)
        while True:
            continuar = input("Quer continuar? [S/N] ").upper().strip()
            if continuar and continuar[0] in "SN":
                break
            print("ERRO! Responda S ou N.")
        print()
        if continuar[0] == "N":
            break


print("=" * 60)
print("{:<5}      {:<10}     {:<15}     {:<5}".format("Cod", "NOME", "Gols", "Total"))
for j, jogador in enumerate(jogadores):
    print(
        "{:^3}        {:<12}  {:<12}          {:<5}".format(
            (j + 1), jogador["nome"], str(jogador["gols"]), jogador["total"]
        )
    )
print("=" * 60)
while True:
    dados = input("Digite o código do jogador para ver seus dados(999 encerra): ")
    if dados.isdigit():
        dados = int(dados)
        if dados == 999:
            print()
            print("{:^60}".format("<<< PROGRAMA ENCERRADO!! >>>"))
            break
        else:
            if (dados) > 0 and (dados) <= len(jogadores):
                print(
                    f"-- Levantamento do Jogador {jogadores[dados - 1]['nome'].upper()}:"
                )
                for i, gol in enumerate(jogadores[dados - 1]["gols"]):
                    print(f"   No {i + 1}º jogo marcou {gol} gols.")
            else:
                print(
                    f"ERRO! Não existe jogador com código {dados}. Tente novamente..."
                )
    else:
        print("Informação inválida! Tente novamente...")

print("=" * 60)
