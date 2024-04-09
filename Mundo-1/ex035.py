# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = input("Digite o valor do primeiro segmento de reta: ")
r2 = input("Digite o valor do segundo segmento de reta: ")
r3 = input("Digite o valor do terceiro segmento de reta: ")

if r1 and r2 and r3:
    reta1 = float(r1)
    reta2 = float(r2)
    reta3 = float(r3)
    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
        print("Esses segmentos de reta podem formar um triângulo.")
    else:
        print("Não é possível formar um triângulo utilizando esses segmentos de reta.")
else:
    print("É necessário informar o valor das 3 retas.")
