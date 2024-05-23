"""Crie um prog que leia nome, ano de nasc e carteira de trab e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date

print("=" * 60)
nome = input("Nome: ")
ano_nasc = input("Ano de Nascimento: ")
cart_trab = input("Carteira de Trabalho (0 se não tem): ")

if nome and ano_nasc.isdigit() and cart_trab.isdigit():

    ano_nasc = int(ano_nasc)
    cart_trab = int(cart_trab)
    data_atual = date.today().year
    idade = data_atual - ano_nasc
    cadastro = {
        "nome": nome,
        "idade": idade,
        "ctps": cart_trab,
    }
    if cart_trab > 0:
        ano_contratacao = input("Ano de Contratação: ")
        salario = input("Salário: R$ ")
        if salario and ano_contratacao.isdigit():
            salario = float(salario)
            ano_contratacao = int(ano_contratacao)
            aposenta = (ano_contratacao - ano_nasc) + 35
            cadastro.update(
                {
                    "contratacao": ano_contratacao,
                    "salario": salario,
                    "aposentadoria": aposenta,
                }
            )
        else:
            print("Informação inválida! Tente novamente...")
    print("-" * 60)

    for k, v in cadastro.items():
        print(f" - {k} tem o valor: {v}")
else:
    print("Informação inválida! Tente novamente...")

print("=" * 60)
