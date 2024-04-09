# Escreva um prog que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
v = input("Insira a velocidade do carro: ")

if v:
    vel = int(v)
    if vel > 80:
        print("Você foi multado. Sua multa custará R$ {:.2f}!".format((vel - 80) * 7))
    else:
        print("Parabens! Você está dentro do limite de velocidade.")
else:
    print("Você não inseriu a velocidade!")
