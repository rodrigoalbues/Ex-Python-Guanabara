# Faça um programa que leia o comprimento do cateto oposto e do cateto djacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hipot = math.hypot(co, ca)

print(
    "O valor da hipotenusa do triângulo retângulo que possui {} como cateto oposto e {} como cateto adjacente é {: .2f}!".format(
        co, ca, hipot
    )
)
