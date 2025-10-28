from doctest import Example
from CRUDpython.database import conectar


def criar_editora(nome):
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            sql="Insert into tbl_editora(nomeeditora)vaues (%s) returning ideditora"

            cursor.execute(sql,(nome,))
            id_nova-editora = cursor.fetchome()[0]
            conn.commit()
            print(f"Editora {nome} inserida com sucesso")
    except Exception as e:
        conn.rollback()
        print(f"erro ao inserir editora:{e}")
    finally:
        conn.close()


def listaEditoras():
    conn = conectar()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from tbl_editora order by nomeeditora")
            editoras = cursor.fetchall()
            if not editoras:
                print("Nenhuma editora encontrada")
                return
            print("\n --- Lista de Editoras ---")
            for editora in editora:
                print(editora)
    except Exception as e:
        print(e)
    finally:
        conn.close()




