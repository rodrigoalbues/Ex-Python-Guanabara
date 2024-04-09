"""Faça um prog que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 seg entre eles."""

from time import sleep

print("Os fogos começaram em:")

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print("FOGO!!!")
