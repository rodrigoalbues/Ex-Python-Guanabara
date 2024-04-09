"""Crie um prog que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere: US$ 1,00 = R$ 3,27"""
r = float(input("Quanto você tem na carteira? R$ "))

d = r / 3.27

print("Você tem R${: .2f} reais que correspondem à US$ {: .2f} dolares".format(r, d))
