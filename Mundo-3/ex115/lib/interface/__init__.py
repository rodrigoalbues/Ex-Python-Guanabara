def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    C = 1
    for i, v in enumerate(lista):
        print(f"\033[33m{i + 1}\033[m - \033[34m{v}\033[m")
    print(linha())
    opc = leiaInt("\033[32mSua Opção: \033[m")
    return opc
