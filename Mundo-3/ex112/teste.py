"""Dentro do pacote utilidadesCeV que criamos no ex111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários."""

import utilidadescev.moeda
import utilidadescev.dado

print("=" * 60)
p = utilidadescev.dado.leiaDinheiro("Digite o preço: R$ ")
utilidadescev.moeda.resumo(p, 35, 22)

print("=" * 60)
