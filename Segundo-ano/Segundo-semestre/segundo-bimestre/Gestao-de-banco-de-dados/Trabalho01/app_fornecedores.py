from database import conectar

# CREATE (inserir)
def criar_fornecedor(nome, cnpj, telefone=None, endereco=None):
    """Insere um novo fornecedor"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO fornecedores (nome, cnpj, telefone, endereco)
            VALUES (%s, %s, %s, %s)
            RETURNING id_fornecedor
            """
            cursor.execute(sql, (nome, cnpj, telefone, endereco))
            id_novo_fornecedor = cursor.fetchone()[0]
            conn.commit()
            print(f"Fornecedor '{nome}' inserido com sucesso! (ID: {id_novo_fornecedor})")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir fornecedor: {e}")
    finally:
        conn.close()


# READ (listar/ler)
def listar_fornecedores():
    """Lista todos os fornecedores cadastrados"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id_fornecedor, nome, cnpj, telefone, endereco
                FROM fornecedores
                ORDER BY nome
            """)
            fornecedores = cursor.fetchall()
            if not fornecedores:
                print("Nenhum fornecedor encontrado.")
                return
            print("\n--- Lista de Fornecedores ---")
            for f in fornecedores:
                print(f"ID: {f[0]}, Nome: {f[1]}, CNPJ: {f[2]}, Telefone: {f[3]}, Endereço: {f[4]}")
    except Exception as e:
        print(f"Erro ao listar fornecedores: {e}")
    finally:
        conn.close()


# UPDATE (atualizar)
def atualizar_fornecedor(id_fornecedor, nome=None, cnpj=None, telefone=None, endereco=None):
    """Atualiza os dados de um fornecedor existente"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            # Monta dinamicamente os campos a atualizar
            campos = []
            valores = []

            if nome:
                campos.append("nome = %s")
                valores.append(nome)
            if cnpj:
                campos.append("cnpj = %s")
                valores.append(cnpj)
            if telefone:
                campos.append("telefone = %s")
                valores.append(telefone)
            if endereco:
                campos.append("endereco = %s")
                valores.append(endereco)

            if not campos:
                print("Nenhum campo informado para atualização.")
                return

            valores.append(id_fornecedor)
            sql = f"UPDATE fornecedores SET {', '.join(campos)} WHERE id_fornecedor = %s"
            cursor.execute(sql, tuple(valores))

            if cursor.rowcount == 0:
                print(f"Nenhum fornecedor encontrado com ID {id_fornecedor}.")
            else:
                conn.commit()
                print(f"Fornecedor ID {id_fornecedor} atualizado com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar fornecedor: {e}")
    finally:
        conn.close()


# DELETE (excluir)
def excluir_fornecedor(id_fornecedor):
    """Exclui um fornecedor pelo seu ID"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM fornecedores WHERE id_fornecedor = %s"
            cursor.execute(sql, (id_fornecedor,))
            if cursor.rowcount == 0:
                print(f"Nenhum fornecedor encontrado com ID {id_fornecedor}. Nada foi excluído.")
            else:
                conn.commit()
                print(f"Fornecedor ID {id_fornecedor} excluído com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao excluir fornecedor: {e}")
        print("Nota: Se este fornecedor estiver sendo referenciado em outra tabela (ex: pedidos),")
        print("o PostgreSQL pode bloquear a exclusão devido a restrições de chave estrangeira.")
    finally:
        conn.close()
