"""Crie um prog que leia vários nrs inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O prog deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

num = 0
rep = ""
media = 0
soma = 0
cont = 0
maior = float("-inf")
menor = float("inf")

while rep != "N":
    num = input("Digite um número inteiro: ")

    if num.isnumeric():
        num = int(num)
        cont += 1
        soma += num
        media = soma / cont

        if num > maior:
            maior = num
        if num < menor:
            menor = num

        rep = input("Gostaria de digitar mais um número?[S/N] ").upper().strip()[0]

        if rep != "S" and rep != "N":
            rep = "N"
            print("Informação inválida!")
    else:
        print("Informação inválida!")
        rep = input("Gostaria de digitar mais um número?[S/N] ").upper().strip()[0]

        if rep != "S" and rep != "N":
            rep = "N"
            print("Informação inválida!")

print(
    """Informações:
      - Quantidade de números digitados -> {}
      - Soma dos números digitados -> {}
      - Média dos números digitados -> {:.2f}
      - Maior números digitado -> {}
      - Menor número digitado -> {}""".format(
        cont, soma, media, maior, menor
    )
)
