from funcoes import adicionar_aula, remover_aula, listar_aulas

def menu():
    while True:
        print('===== Sistema de Agendamento de Aulas =====')
        print('1 - Agendar aula')
        print('2 - Remover aula')
        print('3 - Listar aulas')
        print('0 - Sair')

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dia_aula = input('Digite o dia da aula (Ex.: 02/12): ').capitalize()
            horario_aula = input('Digite o horário da aula (Ex.: 08:15): ')
            adicionar_aula(dia_aula, horario_aula)
                
        elif opcao == "2":
            dia_remover = input("Digite o dia para remover (Ex.: 02/12): ")
            hora_remover = input("Digite o horário que será removido (Ex.: 09:30: )")
            remover_aula(dia_remover, hora_remover)
        
        elif opcao == "3":
            listar_aulas()
            
        elif opcao == "0":
            print('Encerrando...\nSistema de aula finalizado!')
            break

        else:
            print('Opção inválida!')

if __name__ == "__main__":
    menu()
