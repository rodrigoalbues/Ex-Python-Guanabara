# Crie um prog que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input("Digite o nome da cidade: ")
cidadeAjust = cidade.upper().strip()

if cidadeAjust.startswith("SANTO"):
    print('O nome dessa cidade começa com "SANTO"!')
else:
    print('O nome dessa cidade não começa com "SANTO"!')
