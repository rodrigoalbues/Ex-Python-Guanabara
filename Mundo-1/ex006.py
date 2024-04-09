# Crie um algoritmo que leia um nr e mostre o seu dobro, triplo e raiz quadrada.

n = float(input("Digite um número: "))

d = n * 2
t = n * 3
rq = n ** (1 / 2)

print("O número digitado foi: {}".format(n))
print("O seu dobro é: {}".format(d))
print("O seu triplo é: {}".format(t))
print("A raiz quadrada é: {: .2f}".format(rq))