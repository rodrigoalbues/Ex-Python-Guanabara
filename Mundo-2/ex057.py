"""Faça um prog que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = ""

while sexo != "M" or sexo != "F":
    sexo = input("Digite seu sexo [M/F]: ").upper()[0].strip()

    if sexo == "M":
        sexo = "masculino"
        print("Você é do sexo {}, registro feito com sucesso.".format(sexo))
        break
    elif sexo == "F":
        sexo = "feminino"
        print("Você é do sexo {}, registro feito com sucesso.".format(sexo))
        break
    else:
        print("Informação inválida!")
