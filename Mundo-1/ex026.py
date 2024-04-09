"""Faça um prog que leia uma frase pelo teclado e mostre:
   - Quantas vezes aparece a letra 'A'.
   - Em que posição ela aparece a primeira vez.
   - Em que posiçao ela aparece a última vez."""
frase = input("Digite uma frase: ")

fraseMaiusc = frase.upper().strip()

print('Nessa frase aparece a letra "A" {} vezes.'.format(fraseMaiusc.count("A")))
print(
    'A letra "A" aparece pela primeira vez na posição {}.'.format(
        fraseMaiusc.find("A") + 1
    )
)
print(
    'A letra "A" aparece pela última vez na posição {}.'.format(
        fraseMaiusc.rfind("A") + 1
    )
)
