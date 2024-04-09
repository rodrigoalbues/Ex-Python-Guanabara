# Crie um prog que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input("Digite o nome: ")

nomeAjust = nome.upper().strip()

if "SILVA" in nomeAjust:
    print('Essa pessoa tem "SILVA" no nome!')
else:
    print('Essa pessoa não tem "SILVA" no nome!')
