"""Crie um programa onde 4 jogoadores joguem um dado e tenham resultados aleatórios em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencendor tirou o maior nr no dado."""

from random import randint
from time import sleep

print("=" * 60)
jogadores = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6),
}
print("Valores Sorteados:")
print("-" * 60)
for j, v in jogadores.items():
    print(f" O {j} tirou {v}")
    sleep(0.7)
print("-" * 60)
ranking = sorted(
    jogadores.items(), key=lambda x: x[1], reverse=True
)  # Pode ser usado tbm 'key=itemgetter(1)' mas é preciso importar 'from operator import itemgetter'

print("Ranking dos jogadores:")
print("-" * 60)
for i, (jogador, valor) in enumerate(ranking, start=1):
    print("{}º lugar: {} com {} pontos.".format(i, jogador, valor))
    sleep(0.7)
print("=" * 60)
