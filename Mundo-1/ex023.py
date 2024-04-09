# Faça um prog que leia um nr de 0 a 9999 e mostre na tela cada um dos digitos separados. ( unidade, dezena, centena e milhar)
n = int(input("Digite um número entre 0 e 9999: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print("O número {} possui:".format(n))
print("{} unidades".format(u))
print("{} dezenas".format(d))
print("{} centenas".format(c))
print("{} milhares".format(m))
