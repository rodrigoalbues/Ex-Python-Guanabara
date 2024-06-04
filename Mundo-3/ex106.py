"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: Use cores."""


def apoio(topico):
    resp = help(topico)
    return resp


while True:
    print("=" * 60)
    print("SISTEMA DE AJUDA PYHELP".center(60))
    print("-" * 60)
    assunto = input("Função ou Biblioteca (FIM para encerrar)> ").lower().strip()
    print()
    if assunto == "fim":
        break
    print(f"Acessando o comando '{assunto}': ")
    print()
    res = apoio(assunto)

print("-" * 60)
print("PROGRAMA ENCERRADO!".center(60))
print("=" * 60)
