"""Crie um pacote chamado utilidadesCeV que tenha 2 módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos ex 107,108 e 109 para o 1º pacote e mantenha tudo funcionando."""

import utilidadescev.moeda

print("=" * 60)
while True:
    p = input("Digite o preço: R$ ")

    if p:
        utilidadescev.moeda.resumo(p, 20, 12)
        break
    else:
        print("Valor inválido..")
        print("-" * 60)
print("=" * 60)
