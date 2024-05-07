"""Crie um prog que vai ler vários num e colocar em uma lista. Depois disso, mostre:
A) Quantos num foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

numeros = []
print("=" * 80)
while True:
    num = input("Digite um número: ")

    if num.isnumeric():
        num = int(num)
        numeros.append(num)
        print("Número dicionado com sucesso...")
        print("")
        print("-" * 80)
        continuar = input("Deseja continuar? [S/N] ").upper().strip()
        print("")
        if continuar and continuar[0] in "SN":
            if continuar == "N":
                break
        else:
            print("Informação inválida!")
            print()
    else:
        print("Informação inválida!")
        print()
qtd = len(numeros)
ordem = sorted(numeros, reverse=True)
print(f"Você digitou {qtd} elementos, que foram {numeros}.")
print(f"Os valores em ordem decrescente são: {ordem}")
if 5 in numeros:
    print("O número 5 está presente em sua lista.")
else:
    print("O número 5 não está presente em sua lista.")
print("=" * 80)
