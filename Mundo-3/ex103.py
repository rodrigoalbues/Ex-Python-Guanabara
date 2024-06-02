"""Faça um prog que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o nome de um jogador e qts gols ele marcou.
O prog deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

print("=" * 60)


def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


n = input("Nome do jogador: ")
g = input("Número de gols: ")

if g.isdigit():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gols=g)
else:
    ficha(n, g)

print("=" * 60)
