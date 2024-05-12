"""Faça um prog que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 nr entre 1 e 60 p/ cada jogo, cadastrando tudo em uma lista composta."""

from random import sample

print("=" * 80)
print("Gere seus jogos da Mega Sena!!!".center(80))
print("-" * 80)
qtd = input("Digite quantos jogos você gostaria: ")
print()
if qtd.isnumeric():
    qtd = int(qtd)
    for i in range(qtd):
        jogo = sorted(sample(range(1, 61), 6))
        print(f"Jogo {i + 1}: {jogo}")
print()
print("BOA SORTE!!!".center(80))
print("=" * 80)
