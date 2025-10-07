
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))    

def operacoes_matematicas(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao

resultados = operacoes_matematicas (a, b)

print(resultados)