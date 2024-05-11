"""Crie um prog onde o usuário possa digitar 7 valores num e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores parese ímpares em ordem crescente."""

numeros = [[], []]
print("=" * 80)
for i in range(1, 8):
    num = input(f"Digite o {i}º número inteiro: ")
    if num.isnumeric():
        num = int(num)
        if num % 2 == 0:
            numeros[0].append(num)
        else:
            numeros[1].append(num)
    else:
        print("Informação inválida!")
print("-" * 80)
print(f"Em ordem crescente os valores pares digitados foram: {sorted(numeros[0])}")
print(f"Em ordem crescente os valores ímpares digitados foram: {sorted(numeros[1])}")
print("=" * 80)
