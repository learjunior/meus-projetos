
agendamentos = {}

def adicionar_aula(dia, horario):
    aula = {
        'dia': dia,
        'horario': horario
    }
    if dia in agendamentos:
        agendamentos[dia].append(aula)
    else:
        agendamentos[dia]=[aula]
        print(f'Aula adicionada em {dia} às {horario}.')

def listar_aulas():
    if not agendamentos:
        print('Nenhuma aula agendada.')
        return
    for dia, aulas in agendamentos.items():
        print(f'\nDia: {dia}')
        for i, aula in enumerate(aulas, start=1):
            print(f"{i}. {aula['dia']} - {aula['horario']}")

def remover_aula(dia, numero_aula):
    try:
        numero_aula = int(numero_aula)
    except ValueError:
        print("O número precisa ser um inteiro.")
        return False

    if dia in agendamentos and 0 < numero_aula <= len(agendamentos[dia]):
        aula = agendamentos[dia].pop(numero_aula - 1)
        print(f"Aula do dia {aula['dia']} às {aula['horario']} foi removida.")
        if not agendamentos[dia]:
            del agendamentos[dia]
        return True
    else:
        print("Aula não encontrada ou número inválido")
        return False
