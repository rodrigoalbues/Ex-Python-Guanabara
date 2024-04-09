print('====== DESAFIO 01 ======')

nome = input('Qual é o seu nome? ')
print('Olá, {}! Prazer em te conhecer!'.format(nome))

print('')

print('====== DESAFIO 02 ======')

print('Qual a sua data de nascimento?')

dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')

print('Você nasceu no dia {} de {} de {}.'.format(dia, mes, ano))

confirmacao = input('Correto? SIM ou NÃO? ')

if (confirmacao == 'sim'):
    print('OK! Obrigado')
if (confirmacao == 'não'):
    print('Tente novamente!')

print('')

print('====== DESAFIO 03 ======')

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

soma = n1 + n2

print('A soma entre {} e {} números é: {: .2f}'.format(n1, n2, soma))
