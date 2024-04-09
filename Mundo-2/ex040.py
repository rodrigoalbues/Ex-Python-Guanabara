"""Crie um prog que leia 2 notas de um aluno e calcule sua média, mostrando uma msg no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÂO
- Média 7.0 ou superior: APROVADO"""
n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")

if n1 and n2:
    nota1 = float(n1)
    nota2 = float(n2)
    media = (nota1 + nota2) / 2
    if media < 5:
        print("Sua média é {:.1f}, você está REPROVADO.".format(media))
    elif media >= 7:
        print("Sua média é {:.1f}, você está APROVADO.".format(media))
    else:
        print("Sua média foi {:.1f}, você está de RECUPERAÇÃO.".format(media))
else:
    print("Preencha com todas as informações!")
