from database import conectar

# create  (inserir)
def criar_editora(nome):
  """Insere uma nova editora"""
  conn = conectar() #obtém uma nova conexão
  if conn is None:
    return #Se a conexão falhou, não faz nada
  
  try:
    with conn.cursor() as cursor:
      # SQL parametrização para evitar SQL Injection
      sql="Insert into tbl_editora(nomeeditora)" \
      " values (%s) returning ideditora"
      # executa o comando. Passamos os valores como tupla.
      cursor.execute(sql, (nome,))
      # pega o ID da editora de acabamos de inserir
      id_nova_editora = cursor.fetchone()[0]
      # confirma a transação
      conn.commit()
      print(f"Editora '{nome}' inserida com sucesso! (ID: {id_nova_editora})")
  except Exception as e:
    # se der erro, desfaz a transação
    conn.rollback()
    print(f"Erro ao inserir editora: {e}")
  finally:
    conn.close()

# READ (listar/ler)
def lista_editoras():
  """lista todas as editoras cadastradas"""
  conn = conectar()
  if conn is None:
    return
  
  try:
    with conn.cursor() as cursor:
      # select simples para listar editoras
      cursor.execute("Select ideditora, nomeeditora from tbl_editora order by nomeeditora")
      # pega todos os resultado da consulta
      editoras = cursor.fetchall()
      if not editoras:
        print("Nenhuma editora encontrada.")
        return
      print("\n--- Lista de Editoras ---")
      # imprime o conteúdo de editoras
      for editora in editoras:
        # editora[0] é ideditora e editora[1] é nomeeditora
        print(f"ID: {editora[0]}, Nome: {editora[1]}")
  except Exception as e:
    print(f"Erro ao listar editoras: {e}")

  finally:
    conn.close()

# UPDATE (atualizar)
def atualizar_editora(id_editora, novo_nome):
  """Atualiza o nome de um editora existente"""
  conn = conectar()
  if conn is None:
    return

  try:
    with conn.cursor() as cursor:
      sql = "update tbl_editora set nomeeditora = %s where ideditora = %s"
      # A ordem dos parametros da tupla (novo_nome, id_editora) deve bater com a ordem %s no sql
      cursor.execute(sql, (novo_nome, id_editora))
      # cursor.rowcount diz quantas linhas fora afetadas
      if cursor.rowcount == 0:
        print(f"Nenhuma editora encontrada com ID {id_editora}. Nada foi atualizado")
      else: 
        # se afetou alguma linha, commita
        conn.commit()
        print(f"Editora ID {id_editora} atualizada para '{novo_nome}'") 

  except Exception as e:
    conn.rollback
    print(f"Erro ao atualizar editora: {e}")
  finally:
    conn.close()

# DELETE (excluir)
def excluir_editora(id_editora):
  """Excluir uma editora pelo seu ID"""
  conn = conectar()
  if conn is None:
    return

  try:
    with conn.cursor() as cursor:
      sql="delete from tbl_editora where ideditora=%s" 
      cursor.execute(sql, (id_editora,))
      if cursor.rowcount == 0: 
        print(f"Nenhuma editora encontrada com id {id_editora}. Nada foi excluído")
      else: 
        conn.commit()
        print(f"Editora ID {id_editora} excluída com sucesso.")
  except Exception as e:
    conn.rollback
    print(f"Erro ao excluir editora: {e}")
    # explicação didática importante:
    print("Nota: Se esta editora estiver sendo usada por um livro na 'tbl_livro'")
    print("o PostgreSQL irá bloquear a exclusão (erro de chave estrangeira)")
    print("mesmo que seu SQL tenha 'On delete cascade' (isso aplica se aplica a tbl_livro,")
    print("não a tbl_editora sendo referenciada")

  finally:
    conn.close()




  
