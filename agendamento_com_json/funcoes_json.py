"""
import json
import os

ARQUIVO = 'agendamentos.json'

# --- Função auxiliar para carregar e salvar dados ---

def carregar_agendamentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}  # se o arquivo não existe, retorna dicionário vazio


def salvar_agendamentos(agendamentos):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(agendamentos, f, indent=4, ensure_ascii=False)


# --- Funções principais ---

def adicionar_aula(dia, horario, professor):
    agendamentos = carregar_agendamentos()

    if dia not in agendamentos:
        agendamentos[dia] = []

    # Verifica se já existe aula no mesmo horário
    for aula in agendamentos[dia]:
        if aula['horario'] == horario:
            print(f"❌ Já existe uma aula agendada nesse horário ({horario}) para {dia}.")
            return

    agendamentos[dia].append({'dia': dia, 'horario': horario, 'professor': professor})
    salvar_agendamentos(agendamentos)
    print(f"✅ Aula adicionada com sucesso: {dia} - {horario} ({professor})")


def remover_aula(dia, horario):
    agendamentos = carregar_agendamentos()

    if dia not in agendamentos:
        print(f"❌ Não há aulas cadastradas para {dia}.")
        return

    for aula in agendamentos[dia]:
        if aula['horario'] == horario:
            agendamentos[dia].remove(aula)
            if not agendamentos[dia]:
                del agendamentos[dia]  # remove o dia se ficou vazio
            salvar_agendamentos(agendamentos)
            print(f"🗑️ Aula das {horario} removida com sucesso de {dia}.")
            return

    print(f"❌ Nenhuma aula encontrada às {horario} em {dia}.")


def listar_aulas():
    agendamentos = carregar_agendamentos()

    if not agendamentos:
        print("📭 Nenhuma aula agendada.")
        return

    print("\n📅 AULAS AGENDADAS:")
    for dia, aulas_do_dia in agendamentos.items():
        print(f"\n📆 Dia: {dia}")
        for i, aula in enumerate(aulas_do_dia, start=1):
            print(f"  {i}. {aula['horario']} - Professor: {aula['professor']}")
"""