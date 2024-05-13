"""Crie um prog que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

alunos = []
aluno = []
print("=" * 60)
while True:
    nome = input("Nome: ")
    n1 = input("Nota 1: ")
    n2 = input("Nota 2: ")
    if nome and n1 and n2:
        n1 = float(n1)
        n2 = float(n2)
        media = (n1 + n2) / 2
        aluno.append(nome)
        aluno.append(n1)
        aluno.append(n2)
        aluno.append(media)
        alunos.append(aluno[:])
        aluno.clear()
        print("Notas cadastradas com sucesso...")
        print("-" * 60)
        continuar = input("Quer continuar? [S/N] ").upper().strip()
        print()
        if continuar and continuar[0] == "N":
            break
    else:
        print("Informação inválida!")
print("=" * 60)
print("{:<30}".format("Nº    NOME"), end="")
print("{:>7}".format("MÉDIA"))
for p, aluno in enumerate(alunos):
    print("{}     {:<22} {:>7.1f}".format((p + 1), aluno[0], aluno[3]))
print("-" * 60)
while True:
    notas_aluno = input(
        "Digite o código do aluno que deseja ver as notas (999 para encerrar): "
    )
    print()
    if notas_aluno.isdigit():
        notas_aluno = int(notas_aluno)
        if notas_aluno == 999:
            break
        else:
            if (notas_aluno) > 0 and (notas_aluno) <= len(alunos):
                print(
                    f"As notas de {alunos[notas_aluno - 1][0]} são {alunos[notas_aluno - 1][1]} e {alunos[notas_aluno - 1][2]}."
                )
                print("=" * 60)
            else:
                print("Código não cadastrado!")
                print()
    else:
        print("Informação inválida!")
print("<<< PROGRAMA ENCERRADO >>>".center(60))
