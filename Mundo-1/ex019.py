# Um prof quer sortear um dos seus 4 alunos para apagar o quadro. Faça um prog que ajude a ele, lendo o nome deles e escrevendoo nome do escolhido.
from random import randint

aluno1 = input("Insira o primeiro nome: ")
aluno2 = input("Insira o segundo nome: ")
aluno3 = input("Insira o terceiro nome: ")
aluno4 = input("Insira o quarto nome: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = alunos[randint(0, 3)]

print("O aluno que irá apagar o quadro é o aluno {}.".format(sorteado))
