num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
operacao=input("Digite a operação que deseja utilizar: ")

if operacao == "adicao":
    print(num1+num2)
elif operacao == "subtracao":
    print(num1-num2)
elif operacao == "multiplicacao":
        print(num1*num2)
elif operacao == "divisao":
        print(num1//num2)
else:
      print("Você digitou a operação errada! Tente novamente...")
