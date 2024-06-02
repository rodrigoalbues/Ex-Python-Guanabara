"""Crie um prog que tenha uma função chamada voto() que vai receber como parâmetro o ano de nasc de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
- Negado -> menor de 16
- Opcional -> entre 16 e 18, e a partir 65
- Obrigatório -> a partir dos 18 até 65"""


def voto(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 18 <= idade < 65:
        return f" Com {idade} anos: VOTO OBRIGATÓRIO."
    else:
        return f"Com {idade} anos: VOTO OPCIONAL."


print("=" * 60)
ano_nasc = input("Em que ano você nasceu? ")
print("-" * 60)
if ano_nasc.isdigit():
    ano_nasc = int(ano_nasc)
    resultado = voto(ano_nasc)
    print(resultado)
else:
    print("Informação inválida!")

print("=" * 60)
