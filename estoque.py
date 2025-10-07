
"""
O que o sistema precisa fazer:
- Cadastrar produtos (nome, código, quantidade, preço).
- Atualizar entrada e saída de produtos.
- Mostrar lista de produtos em estoque.
- Gerar relatórios (opcional, mais pra frente).
Escolher como armazenar os dados:
- um dicionário ou uma lista em Python.
- evoluir para arquivos .json ou .csv ???
- em breve usar um banco de dados (SQLite/MySQL/PostgreSQL).
"""

estoque = {}

def adicionar_produto(id, nome, quantidade):
    if nome in estoque:
        estoque[nome] =+ quantidade
    else:
        estoque[nome] = quantidade
        print(f'{quantidade} unidades de {nome} foi adicionado ao estoque.')

def mostrar_estoque():
    print(f'/n=== Estoque Atual ===')
    for nome, quantidade in estoque.items():
        print(f'{nome}: {quantidade} unidades')

# remover_produto()
# atualizar_estoque()

