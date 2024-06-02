"""Crie um prog que tenha uma função fatorial() que receba 2 parãmetros: o 1º que indique o nr a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


def fatorial(n=1, show=False):
    """-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    processo = ""
    for i in range(n, 0, -1):
        fat *= i
        if show:
            if i > 1:
                processo += f"{i} x "
            else:
                processo += f"{i} = {fat}"
    if show:
        return f"""O fatorial de {n} é: {fat}
{processo}"""
    else:
        return f"O fatorial de {n} é: {fat}"


print("=" * 60)

num = input("Digite o número que você quer saber o fatorial: ")

if num.isdigit():
    num = int(num)
    process = ""
    while True:
        process = (
            input("Gostaria de ver o processo do fatorial? [S/N] ").upper().strip()
        )
        if process and process[0] in "SN":
            break

    if process == "S":
        res_fat = fatorial(num, True)
    else:
        res_fat = fatorial(num)
    print("-" * 60)
    print(res_fat)
else:
    print("Informação inválida!")
print("=" * 60)

help(fatorial)
