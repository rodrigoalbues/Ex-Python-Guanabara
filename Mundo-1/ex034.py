# Escreva um prog que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule 10%. Para os inferiores ou iguais o aumento é de 15%.
s = input("Digite o valor do salário (R$):")

if s:
    sal = float(s)
    if sal > 1250:
        sal_N = sal * 1.10
    else:
        sal_N = sal * 1.15
    print("O valor do salário após o aumento será de: R$ {:.2f}".format(sal_N))
else:
    print("Valor não informado! Tente novamente.")
