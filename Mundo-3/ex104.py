"""Crie um prog que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico."""


def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m]")

    return n


print("=" * 60)
num = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {num}.")
print("=" * 60)
