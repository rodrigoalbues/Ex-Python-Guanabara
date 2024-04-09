"""Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: 2 lados iguais
-Escaleno: todos os lados diferentes"""

r1 = input("Digite o valor do primeiro segmento de reta: ")
r2 = input("Digite o valor do segundo segmento de reta: ")
r3 = input("Digite o valor do terceiro segmento de reta: ")

if r1 and r2 and r3:
    reta1 = float(r1)
    reta2 = float(r2)
    reta3 = float(r3)
    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:

        if reta1 == reta2 and reta2 == reta3:
            triangulo = "triângulo equilátero"
        elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
            triangulo = "triângulo escaleno"
        else:
            triangulo = "triângulo isósceles"

        print("Esses segmentos de reta podem formar um {}.".format(triangulo))
    else:
        print("Não é possível formar um triângulo utilizando esses segmentos de reta.")
else:
    print(
        "É necessário informar o valor dos 3 segmentos de reta que devem ser números."
    )
