# Faça um prog que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = float(input("Digite o valor do ângulo: "))

angAjust = math.radians(ang)

sen = math.sin(angAjust)
cos = math.cos(angAjust)
tg = math.tan(angAjust)

print(
    "O ângulo de {}° possui o seno de {: .2f}, o cosseno de {: .2f} e a tangente de {: .2f}".format(
        ang, sen, cos, tg
    )
)
