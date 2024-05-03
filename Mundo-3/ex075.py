"""Desenvolva um prog que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o 1º valor 3.
C) Quais foram os nrs pares."""

n1 = input(f"Digite o 1º número: ")
n2 = input(f"Digite o 2º número: ")
n3 = input(f"Digite o 3º número: ")
n4 = input(f"Digite o 4º número: ")

if n1.isnumeric() and n2.isnumeric() and n3.isnumeric() and n4.isnumeric():

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    numeros = (n1, n2, n3, n4)

    cont9 = numeros.count(9)
    print(f"O número 9 apareceu {cont9} vezes.")
    if 3 in numeros:
        pos_do_3 = numeros.index(3)
        print(f"O número 3 apareceu pela primeira vez na {pos_do_3 + 1}ª posição.")
    print(f"Os números pares digitados foram: ", end="")
    for n in numeros:
        if n % 2 == 0:
            print(n, end=" ")


else:
    print("Informação inválida!")
