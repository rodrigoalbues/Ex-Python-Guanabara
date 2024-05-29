"""Faça um prog que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo e realize a contagem.
Seu prog tem que realizar 3 contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada."""

from time import sleep

print("=" * 60)


def contador(inicio, fim, passo):
    for i in range(inicio, (fim + 1), passo):
        print(i, end=" ", flush=True)
        sleep(0.5)


print("Contagem de 1 até 10 de 1 em 1:")
contador(1, 10, 1)
print("FIM!")
print("-" * 60)
print("Contagem de 10 até 0 de 2 em 2:")
contador(10, -2, -2)
print("FIM!")
print("-" * 60)
print("Agora é sua vez de personalizar a contagem!")
init = input("Início: ")
final = input("Fim: ")
intervalo = input("Passo: ")
print(f"Contagem de {init} até {final} de {intervalo} em {intervalo}:")
if init and final and intervalo:
    init = int(init)
    final = int(final)
    intervalo = int(intervalo)
    if intervalo == 0:
        intervalo = 1
    if init > final:
        if intervalo > 0:
            final = final - intervalo - 1
            intervalo *= -1
        else:
            final = final + intervalo

    contador(init, final, intervalo)
    print("FIM!")
else:
    print("Informação inválida!")
print("=" * 60)
