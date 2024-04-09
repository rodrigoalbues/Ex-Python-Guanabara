# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Qual é o valor do produto: R$ "))

pn = p - (p * 0.05)

print("O produto que custava R${: .2f}, na promoção, com 5% de desconto vai custar: R${: .2f}.".format(p,pn))
