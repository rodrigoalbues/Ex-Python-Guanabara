"""Elabore um prog que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

compra = input("Digite o valor do produto: R$ ")
pgto = input(
    """1 - à vista dinheiro / cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
Digite o número correspondente a forma de pagamento: """
)

if compra and pgto:
    c = float(compra)

    if pgto == "1":
        v = c - (c * 0.10)
        print("O valor do produto custará: R$ {:.2f}".format(v))

    elif pgto == "2":
        v = c - (c * 0.05)
        print("O valor do produto custará: R$ {:.2f}".format(v))

    elif pgto == "3":
        p = int(input("Digite quantas parcelas deseja: "))
        v = c
        if p == 2:
            vp = v / p
            print(
                "O valor do produto custará: R$ {:.2f} e sua parcela será de: R$ {:.2f}".format(
                    v, vp
                )
            )
        elif p == 1:
            print("O valor do produto custará: R$ {:.2f}".format(v))
        else:
            print("Opção inválida!")

    elif pgto == "4":
        p = int(input("Digite quantas parcelas deseja: "))
        v = c + (c * 0.20)
        vp = v / p
        print(
            "O valor do produto custará: R$ {:.2f} e sua parcela será de: R$ {:.2f}".format(
                v, vp
            )
        )
    else:
        print("Opção inválida!")

else:
    print("Digite todas as informações solicitadas.")
