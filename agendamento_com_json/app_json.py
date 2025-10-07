"""
from funcoes import adicionar_aula, remover_aula, listar_aulas

def menu():
    while True:
        print("\n=== SISTEMA DE AGENDAMENTO DE AULAS ===")
        print("1️⃣  Adicionar aula")
        print("2️⃣  Remover aula")
        print("3️⃣  Listar aulas")
        print("4️⃣  Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dia = input("Dia da aula: ").capitalize()
            horario = input("Horário (ex: 08:00): ")
            professor = input("Nome do professor: ").title()
            adicionar_aula(dia, horario, professor)

        elif opcao == '2':
            dia = input("Dia da aula a remover: ").capitalize()
            horario = input("Horário da aula: ")
            remover_aula(dia, horario)

        elif opcao == '3':
            listar_aulas()

        elif opcao == '4':
            print("👋 Encerrando o sistema...")
            break

        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == '__main__':
    menu()
"""