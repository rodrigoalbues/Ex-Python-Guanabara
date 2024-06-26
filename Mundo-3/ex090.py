"""Faça um prog que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

print("=" * 60)
nome = input("Nome: ")
media = input(f"Média de {nome}: ")
if media and nome:
    media = float(media)
    if media < 5:
        situacao = "Reprovado"
    elif 5 <= media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"
    print("-" * 60)
    aluno = {"Nome": nome, "Media": media, "situacao": situacao}
    print(
        f"""O nome do aluno é: {aluno["Nome"]}.
Sua média é: {aluno["Media"]}.
Sua situação é: {aluno["situacao"]}"""
    )
else:
    print("Informação inválida!")
print("=" * 60)
