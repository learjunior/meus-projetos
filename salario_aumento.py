salario = float(input("Digite o salário: R$ "))

if salario <= 0.00:
    print("Digite um salário digno!")
else:
    if salario <= 280.00:
        percentual_aumento = 20
    elif salario <= 700.00:
        percentual_aumento = 15
    elif salario <= 1500.00:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

valor_aumento = salario * percentual_aumento / 100
novo_salario = salario + valor_aumento
    
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"O perceptual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
