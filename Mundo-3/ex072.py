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
num = input("Digite um número de 0 a 20: ")

if num.isnumeric():
    num = int(num)
    print(f"O número {num} escrito por extenso é: {num_ext[num]}")
    print("=" * 60)
else:
    print("Informação incorreta!")
