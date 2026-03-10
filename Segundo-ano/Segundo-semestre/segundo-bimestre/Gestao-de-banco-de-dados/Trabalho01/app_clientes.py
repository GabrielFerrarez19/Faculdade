from database import conectar

# CREATE (inserir)
def criar_cliente(nome, email, telefone=None, endereco=None):
    """Insere um novo cliente"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO clientes (nome, email, telefone, endereco)
            VALUES (%s, %s, %s, %s)
            RETURNING id_cliente
            """
            cursor.execute(sql, (nome, email, telefone, endereco))
            id_novo_cliente = cursor.fetchone()[0]
            conn.commit()
            print(f"Cliente '{nome}' inserido com sucesso! (ID: {id_novo_cliente})")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir cliente: {e}")
    finally:
        conn.close()


# READ (listar/ler)
def listar_clientes():
    """Lista todos os clientes cadastrados"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id_cliente, nome, email, telefone, endereco
                FROM clientes
                ORDER BY nome
            """)
            clientes = cursor.fetchall()
            if not clientes:
                print("Nenhum cliente encontrado.")
                return
            print("\n--- Lista de Clientes ---")
            for c in clientes:
                print(f"ID: {c[0]}, Nome: {c[1]}, Email: {c[2]}, Telefone: {c[3]}, Endereço: {c[4]}")
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
    finally:
        conn.close()


# UPDATE (atualizar)
def atualizar_cliente(id_cliente, nome=None, email=None, telefone=None, endereco=None):
    """Atualiza os dados de um cliente existente"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            campos = []
            valores = []

            if nome:
                campos.append("nome = %s")
                valores.append(nome)
            if email:
                campos.append("email = %s")
                valores.append(email)
            if telefone:
                campos.append("telefone = %s")
                valores.append(telefone)
            if endereco:
                campos.append("endereco = %s")
                valores.append(endereco)

            if not campos:
                print("Nenhum campo informado para atualização.")
                return

            valores.append(id_cliente)
            sql = f"UPDATE clientes SET {', '.join(campos)} WHERE id_cliente = %s"
            cursor.execute(sql, tuple(valores))

            if cursor.rowcount == 0:
                print(f"Nenhum cliente encontrado com ID {id_cliente}.")
            else:
                conn.commit()
                print(f"Cliente ID {id_cliente} atualizado com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar cliente: {e}")
    finally:
        conn.close()


# DELETE (excluir)
def excluir_cliente(id_cliente):
    """Exclui um cliente pelo seu ID"""
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            if cursor.rowcount == 0:
                print(f"Nenhum cliente encontrado com ID {id_cliente}. Nada foi excluído.")
            else:
                conn.commit()
                print(f"Cliente ID {id_cliente} excluído com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao excluir cliente: {e}")
        print("Nota: Se este cliente estiver sendo referenciado em outra tabela (ex: pedidos, locações, etc.),")
        print("o PostgreSQL pode bloquear a exclusão devido a restrições de chave estrangeira.")
    finally:
        conn.close()
