import funcoes

while True:
    
    print('===========================\n----- MENU DO ESTOQUE -----\n===========================')
    print('1 - Adicionar produto')
    print('2 - Remover produto')
    print('3 - Entrada no estoque')
    print('4 - Saída no estoque')
    print('5 - Mostrar estoque')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
        try:
            id_produto = int(input('Digite o ID do produto: '))
            produto = input('Digite o nome do produto: ').strip()
            quantidade = int(input('Digite a quantidade: '))
            funcoes.adicionar_estoque(id_produto, produto, quantidade)
        except ValueError:
            print('Entrada inválida: ID e quantidade devem ser números inteiros')
                  
    elif opcao == '2':
        try:
            id_produto = int(input(f'Digite o ID do produto para remover: '))
            funcoes.remover_estoque(id_produto)
        except ValueError:
            print('ID inválido!')
    
    elif opcao == '3':
        try:
            id_produto = int(input('Digite o ID do produto: '))
            quantidade = int(input('Digite a quantidade de entrada: '))
            funcoes.atualizar_estoque(id_produto, quantidade, "entrada")
        except ValueError:
            print('Entrada inválida!')
        
    elif opcao == '4':
        try:
            id_produto = int(input('Digite o ID do produto: '))
            quantidade = int(input('Digite a quantidade de saída: '))
            funcoes.atualizar_estoque(id_produto, quantidade, "saida")
        except ValueError:
            print('Entrada inválida!')

    elif opcao == '5':
        funcoes.mostrar_estoque()
    
    elif opcao == '0':
        print('Sistema finalizado com sucesso!\nAté mais!')
        break

    else:
        print('Opção inválida, tente novamente!')
