
print("Digite seu nome e sua cor predileta!")

user1 = input("Digite seu nome: ")
# cor1 = input("Digite sua cor: ")
user2 = input("Digite seu nome: ")
# cor2 = input("Digite sua cor: ")
user3 = input("Digite seu nome: ")
# cor3 = input("Digite sua cor: ")

dados = {user1 : 'inativo', user2 : 'ativo', user3 : 'inativo'}

for nome, cor in dados.copy().items():
    if cor == 'inativo':
        del dados[nome]

dados_ativos = {}
for nome, cor in dados.items():
    if cor == 'ativo':
        dados_ativos[nome] = cor

print(dados_ativos)
