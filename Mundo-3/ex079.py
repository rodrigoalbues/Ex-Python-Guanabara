"""Crie um prog onde o usuário possa digitar vários valores numéricos (perguntar se deseja continuar) e cadastre-os em uma lista. Caso o num já exista lá dentro, ele não será add. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = []
print("=" * 80)
while True:
    valor = input("Digite um valor: ")
    if valor.isnumeric():
        valor = int(valor)
        if valor not in valores:
            valores.append(valor)
            print("Valor cadastrado com sucesso...")
            print("")
        else:
            print("Elemento não adicionado, esse número já existe em sua lista!")
            print("")
    else:
        print("Informação inválida!")
    continuar = input("Deseha contiuar? [S/N] ").upper().strip()
    print("")

    if continuar and continuar in "SN":
        if continuar == "N":
            break
    else:
        print("Informação inválida!")
        break
    print("-" * 80)
print("")
print(f"Você digitou os valores {sorted(valores)}")
print("=" * 80)
