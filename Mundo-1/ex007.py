# Desenvolva um prog que leia as 2 notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print("A primeira nota foi: {}".format(n1))
print("A segunda nota foi: {}".format(n2))
print("A média das notas é: {: .1f}".format(media))
