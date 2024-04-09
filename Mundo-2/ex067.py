"""Faça um prog que mostre a tabuada de vários nrs, um de cada vez, para cada valor digitado pelo usuário. O prog será interrompido quando o número solicitado for negativo."""

while True:
    num = int(
        input(
            "Digite o número que você gostaria de ver a tabuada (digite um número negativo se quiser parar): "
        )
    )

    if num < 0:
        break
    else:
        for i in range(0, 11):
            print(f"{i} x {num} = {(i*num)}")


print("Programa finalizado!!!")
