"""Crie um prog que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o prog deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

p_maior18 = 0
homens = 0
m_menor20 = 0
pessoas = 0

while True:
    print("=" * 60)
    idade = input("Idade: ")
    sexo = input("Sexo [M/F]: ").upper().strip()

    if idade.isnumeric() and (sexo == "M" or sexo == "F"):
        idade = int(idade)
        pessoas += 1
        if idade > 18:
            p_maior18 += 1
        if sexo == "M":
            homens += 1
        if sexo == "F" and idade < 20:
            m_menor20 += 1
        print("Cadastro realizado com sucesso!")
        print("")
        continuar = input("Gostaria de continuar?[S/N] ").upper().strip()
        print("")

        if continuar == "S" or continuar == "N":
            if continuar == "N":
                break
        else:
            print("Informações inválidas!")
            break

    else:

        print("Informações inválidas!")

print(f"{pessoas} pessoas cadastradas.")
print(f"{p_maior18} são maiores de 18 anos")
print(f"{homens} são homens.")
print(f"{m_menor20} são mulheres menores de 20 anos.")

print("=" * 60)
