"""Crie um prog que vai ler vários num e colocar em uma lista. Depois disso, crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamentes. Ao final, mostre o conteúdo das 3 listas geradas."""

numeros = []
pares = []
impares = []
print("=" * 80)
while True:
    num = input("Digite um número: ")
    if num.isnumeric():
        num = int(num)
        numeros.append(num)
        print("Número adicionado com sucesso...")
        print("-" * 80)
        continuar = input('Deseja continuar ("N" para parar)? ').upper().strip()
        print("")
        if continuar and continuar[0] == "N":
            break
    else:
        print("Informação inválida! Tente novamente.")
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(
    f"""Lista completa: {numeros}
Lista de números pares: {pares}
Lista de números ímpares: {impares}"""
)
print("=" * 80)
