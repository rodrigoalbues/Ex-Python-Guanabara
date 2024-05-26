"""Faça um prog que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a ´rea do terreno."""


def area(l, c):
    area_terreno = l * c
    return area_terreno


print("=" * 60)
print("Medição de Terrenos".center(60))
print("-" * 60)
largura = input("Digite a largura do terreno (m): ")
comprimento = input("Digite o comprimento do terreno (m): ")

if largura and comprimento:
    largura = float(largura)
    comprimento = float(comprimento)
    area_terreno = area(largura, comprimento)
    print(f"A área do terreno {largura} x {comprimento} é: {area_terreno:.2f} m².")
else:
    print("Informação inválida!")
print("=" * 60)
