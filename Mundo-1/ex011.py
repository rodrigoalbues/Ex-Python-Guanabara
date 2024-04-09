# Faça um prog que leia a largura e a altura de uma parede em metros, calcule a sua área e a qtd de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

b = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))

area = b * a

t = area / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {} m².\nVocê precisará de {} litros de tinta para pintar sua parede.".format(b, a, area, t))
