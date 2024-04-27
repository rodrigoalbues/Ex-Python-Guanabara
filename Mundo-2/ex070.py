"""Crie um prog que leia o nome e o preço de vários produtos. O prog deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total de gasto na compra.
B) Qunatos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""

gasto = 0
qtd_prod_mais1000 = 0
nome_prod_barato = ""
menor_preco = float("inf")

print("=" * 60)
while True:
    nome_prod = input("Digite o nome do produto: ")
    preco = input("Digite o valor do produto: R$ ")

    if nome_prod and preco:
        preco = float(preco)
        gasto += preco

        if preco > 1000:
            qtd_prod_mais1000 += 1
        if preco < menor_preco:
            menor_preco = preco
            nome_prod_barato = nome_prod

        print("Cadastro realizado com sucesso!")
        print("")

        continuar = input("Gostaria de continuar[S/N]? ").strip().upper()[0]
        print("-" * 60)

        if continuar == "S" or continuar == "N":
            if continuar == "N":
                break
        else:
            print("Informação inválida!")

    else:
        print("Informações inválidas!")
print(f"O total da sua compra é: R${gasto:.2f}")
print(
    f"Na sua compra existem {qtd_prod_mais1000} produtos com valor maior que R$ 1000.00"
)
print(f"O produto mais barato foi: {nome_prod_barato} que custou R$ {menor_preco:.2f}.")
print("=" * 60)
