"""Crie um prog que leia nome, sexo e idade de várias pessoas em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""

print("=" * 60)
cadastros = []
soma_idade = 0
mulheres = []
acima_media = []
while True:
    nome = input("Nome: ")
    while True:
        sexo = input("Sexo [M/F]: ").upper().strip()
        if sexo and sexo[0] in "MF":
            break
        print("ERRO! Por favor digite M ou F")
    idade = input("Idade: ")
    if nome and idade.isdigit():
        idade = int(idade)
        cadastro = {"nome": nome, "sexo": sexo, "idade": idade}
        cadastros.append(cadastro)
        soma_idade += cadastro["idade"]
        if sexo == "F":
            mulheres.append(nome)
        print("Cadastro realizado com sucesso...")
        print("-" * 60)
        while True:
            continuar = input("Quer continuar? [S/N] ").upper().strip()
            if continuar and continuar[0] in "SN":
                break
            print("ERRO! Por favor digite S ou N")
        print()
        if continuar[0] == "N":
            break
    else:
        print("Informação inválida!")
qtd_pessoas = len(cadastros)
media_idade = soma_idade / qtd_pessoas


print("=" * 60)
print(f"- O grupo tem {qtd_pessoas} pessoas.")
print(f"- A média de idade é de {media_idade:5.2f} anos.")
print(f"- As mulheres cadastradas foram: {mulheres}")
print("Pessoas acima da média de idade:")
for p in cadastros:
    if p["idade"] > media_idade:
        acima_media.append(p["nome"])
        print(f"    {p}")
print(f"- A lista de pessoas que estão com a idade acima da média é: {acima_media}")
print()
print("{:^60}".format("<<< PROGRAMA ENCERRADO >>>"))

print("=" * 60)
