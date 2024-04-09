# Crie um prog que leia um nr real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

n = float(input("Digite um número real: "))
i = math.floor(n)
print("A parte inteira do número {} é {}".format(n, i))
