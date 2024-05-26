"""Faça um prog que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma msg com tamanho adaptável."""

from time import sleep

print("=" * 60)
msg = input("Deixe sua Mensagem: ")


def escreva(msg):
    t_msg = len(msg)
    print("-" * t_msg)
    print(msg)
    print("-" * t_msg)


if msg:
    print("Sua mensagem foi:")
    sleep(0.8)
    escreva(msg)
print("=" * 60)
