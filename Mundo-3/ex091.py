"""Crie um programa onde 4 jogoadores joguem um dado e tenham resultados aleatórios em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencendor tirou o maior nr no dado."""

from random import randint

print("=" * 60)
jogadores = {
    "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
    "jogador 3": randint(1, 6),
    "jogador 4": randint(1, 6),
}
for j, v in jogadores.items():
    print(f" O {j} tirou {v}")
print("-" * 60)
ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("Ranking dos jogadores:")
print("-" * 60)
for i, (jogador, valor) in enumerate(ranking, start=1):
    print("{}º lugar: Jogador {} com {} pontos.".format(i, jogador, valor))
print("=" * 60)
