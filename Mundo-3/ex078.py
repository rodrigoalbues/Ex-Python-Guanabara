"""Faça um prog que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

valores = []
pos_maior = []
pos_menor = []
print("=" * 80)
for i in range(0, 5):
    valor = input(f"Digite um valor para a posição {i}: ")

    if valor.isnumeric():
        valor = int(valor)
        valores.append(valor)
        maior = max(valores)
        menor = min(valores)
for pos in range(len(valores)):
    if valores[pos] == maior:
        pos_maior.append(pos)
    if valores[pos] == menor:
        pos_menor.append(pos)
print("-" * 80)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi o {maior} que foi colocado na posição {pos_maior}.")
print(f"O menor valor digitado foi o {menor} que foi colocado na posição {pos_menor}.")
print("=" * 80)
