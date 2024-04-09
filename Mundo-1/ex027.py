# Faça um prog que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. (Primeiro nome:---- último nome:----)
n = input("Digite o nome completo:")

nome = n.strip().split(" ")
i = len(nome)

print("O primeiro nome é {} e o último nome é {}".format(nome[0], nome[i - 1]))
