
estoque = {}

def adicionar_estoque(id_produto, produto, quantidade):
    if id_produto in estoque:
        print(f'❌ Já existe um produto com o ID {id_produto}.')
    else:
        estoque[id_produto] = {'nome': produto, 'quantidade': quantidade}
        print(f'{quantidade} unidades de {produto} foi adicionado ao estoque.')

def mostrar_estoque():
    if not estoque:
        print(f'O estoque está vazio.')
    else:
        print(f'\n=== Estoque Atual ===\n')
        for id_produto, dados in estoque.items():
            print(f'ID: {id_produto} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']}')

def atualizar_estoque(id_produto, quantidade, operacao = "entrada"):
    if id_produto not in estoque:
        print(f'Produto com ID {id_produto} não encontrado!')
        return
    
    if operacao == "entrada":
        estoque[id_produto]["quantidade"] += quantidade
        print(f"Entrada de {quantidade} unidades adicionadas ao produto {estoque[id_produto]['nome']}.")
    
    elif operacao == "saida":
        if estoque[id_produto]["quantidade"] >= quantidade:
            estoque[id_produto]["quantidade"] -= quantidade
            print(f"Saída de {quantidade} unidades do produto {estoque[id_produto]['nome']}.")
        else:
            print(f"Estoque insufciente para {quantidade} unidade (s) de {estoque[id_produto]['nome']}.")
    
    else:
        print(f'Operação inválida. Use ENTRADA ou SAIDA.')

def remover_estoque(id_produto):
    if id_produto in estoque:
        removido = estoque.pop(id_produto)
        print(f'O produto {removido['nome']} foi removido do estoque.')
    else:
        print(f'Produto com ID {id_produto} não encontrado.')


























"""
import json
import os

# Dicionário global do estoque
estoque = {}

# ------------------ SALVAR / CARREGAR JSON ------------------
def salvar_arquivo(arquivo='estoque.json'):
    produtos = []
    for id_prod, dados in estoque.items():
        produtos.append({
            "id": id_prod,
            "nome": dados["nome"],
            "quantidade": dados["quantidade"]
        })
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)

def carregar_arquivo(arquivo='estoque.json'):
    if not os.path.exists(arquivo):
        return
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            produtos = json.load(f)
        estoque.clear()
        for p in produtos:
            estoque[int(p['id'])] = {'nome': p['nome'], 'quantidade': int(p['quantidade'])}
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")

# ------------------ OPERAÇÕES ------------------
def adicionar_estoque(id_produto, produto, quantidade):
    if id_produto in estoque:
        print(f"❌ Já existe um produto com o ID {id_produto}.")
    else:
        estoque[id_produto] = {'nome': produto, 'quantidade': quantidade}
        print(f"✅ {quantidade} unidades de '{produto}' adicionadas (ID {id_produto}).")
        salvar_arquivo()

def mostrar_estoque():
    if not estoque:
        print("📦 O estoque está vazio.")
    else:
        print("\n=== Estoque Atual ===\n")
        for id_produto, dados in estoque.items():
            print(f"ID: {id_produto} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']}")

def atualizar_estoque(id_produto, quantidade, operacao="entrada"):
    if id_produto not in estoque:
        print(f"❌ Produto com ID {id_produto} não encontrado.")
        return

    if operacao == "entrada":
        estoque[id_produto]["quantidade"] += quantidade
        print(f"📦 Entrada de {quantidade} unidades no produto '{estoque[id_produto]['nome']}'.")
    elif operacao == "saida":
        if estoque[id_produto]["quantidade"] >= quantidade:
            estoque[id_produto]["quantidade"] -= quantidade
            print(f"📤 Saída de {quantidade} unidades do produto '{estoque[id_produto]['nome']}'.")
        else:
            atual = estoque[id_produto]["quantidade"]
            print(f"❌ Estoque insuficiente. Há {atual} unidade(s) e tentou remover {quantidade}.")
    else:
        print("❌ Operação inválida.")
    salvar_arquivo()

def remover_estoque(id_produto):
    if id_produto in estoque:
        removido = estoque.pop(id_produto)
        print(f"🗑️ O produto '{removido['nome']}' (ID {id_produto}) foi removido.")
        salvar_arquivo()
    else:
        print(f"❌ Produto com ID {id_produto} não encontrado.")

"""