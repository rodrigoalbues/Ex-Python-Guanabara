# Desenvolva um prog que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.
d = input("Digite a distânia em Km para o local de destino: ")

if d:
    dist = float(d)
    if dist <= 200:
        valor = dist * 0.50
    else:
        valor = dist * 0.45
    print("O preço da sua passagem é R${:.2f}.".format(valor))
else:
    print("Você não digitou a distância! Tente novamente.")
