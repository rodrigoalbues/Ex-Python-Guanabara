"""Escreva um prog que leia um nr n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""

n = input("Digite qunatos termos da sequência de Fibonacci você gostaria de ver: ")

if n.isnumeric():
    print("-" * 60)
    n = int(n)
    t1 = 0
    t2 = 1

    cont = 2
    print(t1, end="->")
    print(t2, end="->")
    seq = t1 + t2
    while cont < n - 1:
        print(seq, end="->")
        t1 = t2
        t2 = seq
        cont += 1
        seq = t1 + t2
    print(seq)
    print("-" * 60)
else:
    print("Informação inválida!")
