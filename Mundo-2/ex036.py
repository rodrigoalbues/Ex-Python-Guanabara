# Escreva um prog para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em qts anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
vc = input("Qual o valor da casa? ")
s = input("Qual o seu salário? ")
a = input("Vai pagar em quantos anos? ")

if vc and s and a:
    valor_casa = float(vc)
    sal = float(s)
    tempo = int(a) * 12
    p_mensal = valor_casa / tempo
    margem = sal * 0.3
    if p_mensal > margem:
        print(
            "Seu empréstimo foi negado, pois a prestação fica R${:.2f} e sua margem de crédito é de R${:.2f}.".format(
                p_mensal, margem
            )
        )
    else:
        print("Empréstimo concedido. O valor mensal da prestação é de R${:.2f}.".format(p_mensal))

else:
    print("Preencha todas as informações!")
