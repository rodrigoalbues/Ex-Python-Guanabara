#Escreva um prog que converta um temperatura digitada em °C para °F.
c = float(input('Qual é a temperatura em °C? '))

f = ((9 * c) / 5) + 32

print('A temperatura de {} °C corresponde a {} °F!'.format(c, f))