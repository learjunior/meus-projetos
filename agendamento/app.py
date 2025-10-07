import funcoes

while True:
    print('===== Sistema de Agendamento de Aulas =====')
    print('1 - Agendar aula')
    print('2 - Listar aulas')
    print('3 - Remover aula')
    print('0 - Sair')

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        try:
            dia_aula = input('Digite o dia da aula (Ex.: 99/99): ')
            hora_aula = input('Digite o horário da aula (Ex.: 99:99): ')
            funcoes.adicionar_aula(dia_aula, hora_aula)
        except ValueError:
            print(f'Dia e horário não está de acordo com o modelo.')
    
    elif opcao == "2":
        funcoes.listar_aulas()
    
    elif opcao == "3":
        funcoes.listar_aulas()
        dia_aula = input("Digite o dia da aula (Ex.: 99/99): ").strip()
        try:
            numero = int(input('Digite o número da aula: ').strip())
            if not funcoes.remover_aula(dia_aula, numero):
                print("Aula não encontrada ou número inválido!")
        except ValueError:
            print(f'O dia não está de acordo com o modelo ou não existe agendamento.')

    elif opcao == "0":
        print('Sistema de aula finalizado!')
        break

    else:
        print('Entrada inválida!')
