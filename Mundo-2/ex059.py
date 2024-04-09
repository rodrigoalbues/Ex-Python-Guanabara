"""Crie um prog que leia 2 valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

valor1 = input("Digite o 1º valor: ")
valor2 = input("Digite o 2º valor: ")

op = 0

while op != 5:

    if valor1 and valor2:
        valor1 = float(valor1)
        valor2 = float(valor2)

        print(
            """Qual operação deseja realizar?
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos números
          [5] sair do programa"""
        )
        op = input("Digite sua opção: ")

        if op == "1":
            soma = valor1 + valor2
            print("A soma de {:.2f} e {:.2f} é {:.2f}.".format(valor1, valor2, soma))
        elif op == "2":
            multi = valor1 * valor2
            print(
                "O produto de {:.2f} e {:.2f} é {:.2f}.".format(valor1, valor2, multi)
            )
        elif op == "3":
            if valor1 > valor2:
                maior = valor1
            else:
                maior = valor2
            print(
                "Entre os números {:.2f} e {:.2f} o maior é {:.2f}".format(
                    valor1, valor2, maior
                )
            )
        elif op == "4":
            print("Informe seus novos números.")
            valor1 = input("Digite o 1º valor: ")
            valor2 = input("Digite o 2º valor: ")

        elif op == "5":
            print("Você finalizou o programa!")
            break
        else:
            print("Opção válida!")
        
        print("-" * 50)
    else:
        print("Digite os 2 valores!")
