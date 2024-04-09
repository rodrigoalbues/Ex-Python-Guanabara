"""Crie um prog que leia vários nrs inteiros pelo teclado. O prog só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos nrs foram digitados e qual foi a soma entre eles (desconsiderando o flag)"""

cont = 0
soma = 0
while True:
    num = input("Digite um número inteiro (999 para parar): ")
    if num.isnumeric():
        num = int(num)
        if num == 999:
            break
        else:
            cont += 1
            soma += num
    else:
        print("Informação inválida! Tente novamente.")
print(f"Você digitou {cont} números e a soma deles é: {soma}.")
