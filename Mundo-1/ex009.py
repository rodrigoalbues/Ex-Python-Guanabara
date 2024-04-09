# Faça um prog que leia um nr inteiro qualquer e mostre na tela a sua tabuada.
n = int(input("Digite um número para ver sua tabuada: "))

tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('-' * 15)
for i in tab:
    print('  {} x {:2} = {}'.format(n, i, (n * i)))

print('-' * 15)
