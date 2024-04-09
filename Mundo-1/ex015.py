# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Digite a quilometragem percorrida(Km): "))
dia = int(input("Digite quantos dias de aluguel: "))

vDiaria = dia * 60
vKm = km * 0.15
vTotal = vDiaria + vKm

print("A quilometragem percorrida foi de {} Km".format(km))
print("O período alugado foi de {} dias.".format(dia))
print("O valor total do aluguel é: R${: .2f}".format(vTotal))
