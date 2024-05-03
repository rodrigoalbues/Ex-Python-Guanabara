"""Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação (classificação final de 2023). Depois mostre:
A) Apenas os 5 primeiros colocados.
B) os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da chapecoense (trocado pelo Flamengo)."""

times = (
    "Palmeiras",
    "Grêmio",
    "Atlético-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco da Gama",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG",
)

print("=" * 80)
print(" Classificação final do Brasileirão 2023 ".center(80))
print("=" * 80)
print("")

primeiros5 = times[:5]
zr = times[-4:]
ordem_alfabetica = sorted(times)
flamengo = times.index("Flamengo")
print(f"Os cinco primeiros colocados foram: {primeiros5}")
print("-" * 80)
print(f"Os quatro últimos colocados foram: {zr}")
print("-" * 80)
print(
    f"Os times que disputaram o Brasileirão de 2023 em ordem alfabética foram: {ordem_alfabetica}"
)
print("-" * 80)
print(f"O Flamengo terminou na {flamengo + 1}ª colocação.")
print("")
print("=" * 80)
