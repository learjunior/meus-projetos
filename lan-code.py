"""
def minha_funcao():
    nome = "Junior"
    idade = "20"
    print(f"Essa é minha função! Prazer, {nome}! Sua idade é {idade}")

minha_funcao()

def somar(n1, n2):
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} igual a {resultado}")

somar(5,10)

def saudacao(nome):
    print(f"Prazer, {nome}")

saudacao("Junior")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

resultado_da_soma = somar(5,15)
resultado_de_outra_soma = somar(7, 8)
print(f"Fizemos duas somas, a primeira resultando em {resultado_da_soma}, e a segunda o resultou em {resultado_de_outra_soma}")

def verificar_par(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é ímpar")

verificar_par(int(input("Digite o número: ")))


def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite o número: "))

if verificar_par(numero):
    print(f"O número é par!")
else:
    print(f"O número é ímpar!")


def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

soma_da_lista = somar_lista(6, 2, 7, 9)
print(f"O resultado é {soma_da_lista}")
"""

def cont_regressivo(numero):
    while True:
        print(numero)
        numero -= 1
        if numero <= 0:
            break

n1 = int(input("Digite o número: "))

cont_regressivo(n1)