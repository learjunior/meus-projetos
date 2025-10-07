import json
import os

ARQUIVO = "agendamento_com_json/agendamentos.json"

def carregar_agendamentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding = 'utf-8') as f:
            return json.load(f)
    return {}

def salvar_agendamentos(agendamentos):
    with open(ARQUIVO, 'w', encoding = 'utf-8') as f:
        json.dump(agendamentos, f, indent = 4, ensure_ascii = False)

def adicionar_aula(dia, horario):
    agendamentos = carregar_agendamentos()

    if dia not in agendamentos:
        agendamentos[dia] = []
    
    for aula in agendamentos[dia]:
        if aula['horario'] == horario:
            print(f"Já existe uma aula agendada no dia {dia} às {horario}")
            return
    agendamentos[dia].append({'dia': dia, 'horario': horario})
    salvar_agendamentos(agendamentos)
    print(f"Aula adicionada com sucesso: {dia} às {horario}")

def listar_aulas():
    agendamentos = carregar_agendamentos()

    if not agendamentos:
        print('Nenhuma aula agendada.')
        return
    
    print("\nAULAS AGENDADAS: ")
    for dia, aulas_do_dia in agendamentos.items():
        print(f"\nDia: {dia}")
        for i, aula in enumerate(aulas_do_dia, start = 1):
            print(f"{i}. {aula['horario']}")

def remover_aula(dia, horario):
    agendamentos = carregar_agendamentos()

    if dia not in agendamentos:
        print(f"Não há aulas cadastradas para o dia {dia}.")
        return
    
    for aula in agendamentos[dia]:
        if aula['horario'] == horario:
            agendamentos[dia].remove(aula)
            if not agendamentos[dia]:
                del agendamentos[dia]
            salvar_agendamentos(agendamentos)
            print(f"Aula das {horario} removida com sucesso do dia {dia}.")
            return
        
    print(f"Nenhuma aula encontrada às {horario} no dia {dia}.")
