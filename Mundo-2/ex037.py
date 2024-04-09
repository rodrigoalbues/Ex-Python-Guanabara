"""Escreva um prog que leia um nr inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

n = input("Digite um número inteiro: ")
b = input(
    """Bases de conversão:
    1-binário
    2-para octal
    3-hexadecimal
Digite o número correspondente a base de conversão que deseja: """
)
if n and b:
    nDigitado = int(n)

    if b == "1":
        nExibido = bin(nDigitado)
        base = "binária"
    elif b == "2":
        nExibido = oct(nDigitado)
        base = "octal"
    elif b == "3":
        nExibido = hex(nDigitado)
        base = "hexadecimal"

    if b != "1" and b != "2" and b != "3":
        print("Opção inválida. Tente novamente!")
    else:

        print(
            "O número {} convertido para a base {} é igual a {}.".format(
                nDigitado, base, nExibido[2:]
            )
        )

else:
    print("Preencha todas as informações!")
