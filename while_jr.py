

while True:
    numero = input("Insira um número (ou 'sair' para encerrar): ")

    if numero.lower() == "sair":
        print('Encerrando...')
        break
    
    if numero.isdigit():
        print('Você digitou um número inteiro!')
    else:
        try:
            valor = float(numero)
            if valor.is_integer():
                print('Você digitou um número inteiro!')
            else:
                print('Você digitou um número decimal!')

            if valor <= 0:
                print('Observação: número menor ou igual a zero')

        except:
            print('Isso não é número válido!')

