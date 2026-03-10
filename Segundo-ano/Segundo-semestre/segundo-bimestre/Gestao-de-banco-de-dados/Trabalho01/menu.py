from app_clientes import criar_cliente, listar_clientes, atualizar_cliente, excluir_cliente
from app_fornecedores import criar_fornecedor, listar_fornecedores, atualizar_fornecedor, excluir_fornecedor

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("     SISTEMA DE GESTÃO DE BANCO DE DADOS")
        print("="*50)
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Fornecedores")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_fornecedores()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


def menu_clientes():
    """Menu de gerenciamento de clientes"""
    while True:
        print("\n" + "-"*50)
        print("     GERENCIAMENTO DE CLIENTES")
        print("-"*50)
        print("1. Criar novo cliente")
        print("2. Listar todos os clientes")
        print("3. Atualizar cliente")
        print("4. Excluir cliente")
        print("0. Voltar ao menu principal")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            criar_novo_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente_menu()
        elif opcao == "4":
            excluir_cliente_menu()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")


def criar_novo_cliente():
    """Função auxiliar para criar um novo cliente"""
    print("\n--- Criar Novo Cliente ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome é obrigatório!")
        return
    
    email = input("Email: ").strip()
    if not email:
        print("Email é obrigatório!")
        return
    
    telefone = input("Telefone (opcional): ").strip()
    if not telefone:
        telefone = None
    
    endereco = input("Endereço (opcional): ").strip()
    if not endereco:
        endereco = None
    
    criar_cliente(nome, email, telefone, endereco)


def atualizar_cliente_menu():
    """Função auxiliar para atualizar um cliente"""
    print("\n--- Atualizar Cliente ---")
    try:
        id_cliente = int(input("ID do cliente a ser atualizado: ").strip())
    except ValueError:
        print("ID deve ser um número inteiro!")
        return
    
    print("\nDeixe em branco os campos que não deseja atualizar:")
    nome = input("Nome: ").strip()
    if not nome:
        nome = None
    
    email = input("Email: ").strip()
    if not email:
        email = None
    
    telefone = input("Telefone: ").strip()
    if not telefone:
        telefone = None
    
    endereco = input("Endereço: ").strip()
    if not endereco:
        endereco = None
    
    atualizar_cliente(id_cliente, nome, email, telefone, endereco)


def excluir_cliente_menu():
    """Função auxiliar para excluir um cliente"""
    print("\n--- Excluir Cliente ---")
    try:
        id_cliente = int(input("ID do cliente a ser excluído: ").strip())
    except ValueError:
        print("ID deve ser um número inteiro!")
        return
    
    confirmacao = input(f"Tem certeza que deseja excluir o cliente ID {id_cliente}? (s/n): ").strip().lower()
    if confirmacao == "s":
        excluir_cliente(id_cliente)
    else:
        print("Operação cancelada.")


def menu_fornecedores():
    """Menu de gerenciamento de fornecedores"""
    while True:
        print("\n" + "-"*50)
        print("     GERENCIAMENTO DE FORNECEDORES")
        print("-"*50)
        print("1. Criar novo fornecedor")
        print("2. Listar todos os fornecedores")
        print("3. Atualizar fornecedor")
        print("4. Excluir fornecedor")
        print("0. Voltar ao menu principal")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            criar_novo_fornecedor()
        elif opcao == "2":
            listar_fornecedores()
        elif opcao == "3":
            atualizar_fornecedor_menu()
        elif opcao == "4":
            excluir_fornecedor_menu()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")


def criar_novo_fornecedor():
    """Função auxiliar para criar um novo fornecedor"""
    print("\n--- Criar Novo Fornecedor ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome é obrigatório!")
        return
    
    cnpj = input("CNPJ: ").strip()
    if not cnpj:
        print("CNPJ é obrigatório!")
        return
    
    telefone = input("Telefone (opcional): ").strip()
    if not telefone:
        telefone = None
    
    endereco = input("Endereço (opcional): ").strip()
    if not endereco:
        endereco = None
    
    criar_fornecedor(nome, cnpj, telefone, endereco)


def atualizar_fornecedor_menu():
    """Função auxiliar para atualizar um fornecedor"""
    print("\n--- Atualizar Fornecedor ---")
    try:
        id_fornecedor = int(input("ID do fornecedor a ser atualizado: ").strip())
    except ValueError:
        print("ID deve ser um número inteiro!")
        return
    
    print("\nDeixe em branco os campos que não deseja atualizar:")
    nome = input("Nome: ").strip()
    if not nome:
        nome = None
    
    cnpj = input("CNPJ: ").strip()
    if not cnpj:
        cnpj = None
    
    telefone = input("Telefone: ").strip()
    if not telefone:
        telefone = None
    
    endereco = input("Endereço: ").strip()
    if not endereco:
        endereco = None
    
    atualizar_fornecedor(id_fornecedor, nome, cnpj, telefone, endereco)


def excluir_fornecedor_menu():
    """Função auxiliar para excluir um fornecedor"""
    print("\n--- Excluir Fornecedor ---")
    try:
        id_fornecedor = int(input("ID do fornecedor a ser excluído: ").strip())
    except ValueError:
        print("ID deve ser um número inteiro!")
        return
    
    confirmacao = input(f"Tem certeza que deseja excluir o fornecedor ID {id_fornecedor}? (s/n): ").strip().lower()
    if confirmacao == "s":
        excluir_fornecedor(id_fornecedor)
    else:
        print("Operação cancelada.")


if __name__ == "__main__":
    menu_principal()

