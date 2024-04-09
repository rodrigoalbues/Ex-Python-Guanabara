"""Faça um prog que calcule a soma entre todos os nrs ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

print(
    "Escolha o intervalo de números inteiros que gostaria de saber a soma dos números ímpares e múltiplos de 3. (o primeiro deve ser o menor número.)"
)
intInf = input("Digite o primeiro número: ")
intSup = input("Digite o segundo número: ")

s = 0
cont = 0
if intInf and intSup:
    n1 = int(intInf)
    n2 = int(intSup)

    for i in range(n1, n2 + 1):
        if i % 2 != 0 and i % 3 == 0:
            s = s + i
            cont = cont + 1
    print(
        "A soma dos {} números ímpares e que são múltiplos de 3 no intervalo entre {} e {} é:  {}".format(
            cont, n1, n2, s
        )
    )
else:
    print("Digite todas as informações!")
