"""Desenvolva um prog que leia o nome, idade e o sexo de 4 pessoas. No final do prog, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos."""

soma_idade = 0
digitado = 0
media_idade = 0
h_mais_velho = ""
idade_h_mais_velho = float("-inf")
m_menor = 0


for i in range(1, 5):
    nome = input("Digite o nome da {}ª pessoa: ".format(i))
    idade = input("Digite a idade {}ª pessoa: ".format(i))
    sexo = input("Digite o sexo {}ª pessoa (masc = M e fem = F): ".format(i)).upper()

    if nome and sexo and idade.isnumeric():
        digitado += 1
        idade = int(idade)
        soma_idade += idade

        if sexo == "M" and idade > idade_h_mais_velho:
            h_mais_velho = nome
            idade_h_mais_velho = idade
        elif sexo == "F" and idade < 20:
            m_menor += 1
        elif sexo != "M" and sexo != "F":
            digitado = 0

media_idade = soma_idade / 4

if digitado == 0:
    print("Digite corretamente todas as informações solicitadas!")
else:
    print("A média de idade do grupo é: {}.".format(media_idade))
    print(
        "O homem mais velho do grupo com {} anos é o {}.".format(
            idade_h_mais_velho, h_mais_velho
        )
    )
    print("No grupo existem {} mulheres com menos de 20 anos.".format(m_menor))
