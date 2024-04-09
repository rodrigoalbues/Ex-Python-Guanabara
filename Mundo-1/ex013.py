# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento.
sa = float(input("Qual o salário atual: R$ "))

sn = sa * 1.15

print("O salário do funcionário que era de R${: .2f}, após o aumento de 15% o passou a ser de R$ {: .2f}.".format(sa,sn))
