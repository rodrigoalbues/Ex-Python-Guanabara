# O mesmo prof do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um prog que leia o nome dos 4 alunos e mostre a ordem sorteda.
import random

aluno1 = input("Insira o primeiro nome: ")
aluno2 = input("Insira o segundo nome: ")
aluno3 = input("Insira o terceiro nome: ")
aluno4 = input("Insira o quarto nome: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("A ordem de apresentação será:\n{}".format(alunos))
