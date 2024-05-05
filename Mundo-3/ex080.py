"""Crie um prog onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort(). No final, mostre a lista ordenada na tela."""

valores = []

for p, i in enumerate(range(0, 5)):
    valor = input("Digite um valor: ")
    if valor.isnumeric():
        valor = int(valor)
        if p == 0:
            valores.insert(0, valor)
            print(p)
        else:
            if valor >= valores[p - 1]:

                valores.insert(p, valor)
            else:
                if valor < valores[p - 1]:
                    print(valores, p)
print(valores)

# nao funciona ainda
