import os
import json
import random

Diretorio = os.path.dirname(os.path.abspath(__file__))
Arquivo_Json = os.path.join(Diretorio, "usuarios.json")

def carregar_usuarios():
    try:
        with open(Arquivo_Json, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        conteudo = arquivo.read()
        if not conteudo:
            return []
        return json.loads(conteudo)
    
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):
    with open(Arquivo_Json, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

usuarios = carregar_usuarios()

def menu():
    print("=Menu de Cadastros=")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuários")
    print("3 - Excluir Usuário")
    print("4 - Sair")

def opcao_1():
    nome = input("Digite o nome do usuário: ")

    while True:
        codigo_id = random.randint(1000, 9999)
        if all(usuario['ID'] != codigo_id for usuario in usuarios):
            break

    usuario = {
        'nome': nome,
        'ID': codigo_id,
    }
    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    print(f"Usuário {nome} cadastrado com sucesso, ID: {codigo_id}")

def opcao_2():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Lista de Usuários:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, ID: {usuario['ID']}")



def opcao_3():
        codigo_id = int(input("Digite o ID do usuário a ser excluído: "))
        for usuario in usuarios:
            if usuario['ID'] == codigo_id:
                confirmacao = input("Tem certeza que deseja excluir o usuário? (s/n): ")
                if confirmacao.lower() == "s":
                    usuarios.remove(usuario)
                    salvar_usuarios(usuarios)
                    print(f"Usuário {usuario['ID']} excluído com sucesso.")
                    return
                else:
                    print("Exclusão cancelada.")
        else:
            print(f"Usuário {codigo_id} não encontrado.")

def opcao_4():
    print("Saindo do sistema de cadastros.")

def opcao_invalida():
    print("Opção inválida, tente novamente.")
    

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        opcao_1()
    elif escolha == "2":
        opcao_2()
    elif escolha == "3":
        opcao_3()
    elif escolha == "4":
        opcao_4()
        break
    else:
        opcao_invalida()