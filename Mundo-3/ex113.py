"""Reescreva a função leiaInt() que fizemos no ex104, incluindo agora a possibilidade da digitação de um nr de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


print("=" * 60)
n_int = leiaInt("Digite um número inteiro: ")
n_float = leiaFloat("Digite um número real: ")
print(f"O número inteiro digitado foi {n_int} e o real foi {n_float}")
print("=" * 60)
