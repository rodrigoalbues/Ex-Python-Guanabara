""" Crie um prog que leia vários nrs inteiros pelo teclado. O prog só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos nrs foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

num = 0
cont = 0
soma = 0
while num != 999:
    num = input("Digite um número inteiro (Quando quiser parar digite 999): ")

    if num.isnumeric():
        num = int(num)
        if num != 999:
            cont += 1
            soma += num
    else:
        print("Informação inválida!")
print("Você digitou {} números e a soma deles é: {}.".format(cont, soma))
