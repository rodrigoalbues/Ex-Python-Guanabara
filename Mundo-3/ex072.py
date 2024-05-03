"""Crie um prog que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu prog deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

num_ext = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
print("=" * 60)

while True:

    num = input("Digite um número de 0 a 20: ")

    if num.isnumeric():
        num = int(num)
        if num >= 0 and num <= 20:
            print(f"O número {num} escrito por extenso é: {num_ext[num]}")
            print("")
            continuar = input("Quer continuar [S/N] ? ").upper().strip()
            print("=" * 60)
            if continuar and continuar[0] in ("SN"):
                if continuar == "N":
                    break
            else:
                print("Informação inválida. Tente novamente!")
                print("")

        else:
            print("Informação inválida. Tente novamente!")
            print("")
    else:
        print("Informação incorreta!")
        print("")
