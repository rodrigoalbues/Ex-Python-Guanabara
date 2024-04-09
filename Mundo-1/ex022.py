"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas minusculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome"""

nome = input("Digite o nome completo: ")
nome.strip()
espaco = nome.find(" ")

maius = nome.upper()
minusc = nome.lower()
qta_l = len(nome) - nome.count(" ")

print("Nome em letras maiúsculas: {}".format(maius))
print("Nome em letras minúsculas: {}".format(minusc))
print("Esse nome possui {} letras.".format(qta_l))
print("O primeiro nome é: {}".format(nome[:espaco].capitalize()))
print("O primeiro nome tem {} letras.".format(nome.find(" ")))
