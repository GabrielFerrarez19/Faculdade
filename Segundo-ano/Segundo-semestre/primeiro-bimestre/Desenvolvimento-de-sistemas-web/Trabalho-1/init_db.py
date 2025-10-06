

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models


models.Base.metadata.create_all(bind=engine)

def init_db():

    db = SessionLocal()
    
    try:

        if db.query(models.Categoria).count() > 0:
            print("⚠️  O banco já possui dados. Pulando inicialização.")
            return
        
        print("🚀 Inicializando banco de dados com dados de exemplo...")
        
        
        categorias_exemplo = [
            models.Categoria(nome="Eletrônicos"),
            models.Categoria(nome="Roupas"),
            models.Categoria(nome="Livros"),
            models.Categoria(nome="Casa e Jardim"),
        ]
        
        for categoria in categorias_exemplo:
            db.add(categoria)
        
        db.commit()
        
        
        categorias_db = db.query(models.Categoria).all()
        categoria_eletronicos = next(c for c in categorias_db if c.nome == "Eletrônicos")
        categoria_roupas = next(c for c in categorias_db if c.nome == "Roupas")
        categoria_livros = next(c for c in categorias_db if c.nome == "Livros")
        categoria_casa = next(c for c in categorias_db if c.nome == "Casa e Jardim")
        
            
        produtos_exemplo = [
            models.Produto(nome="Smartphone iPhone", preco=3999.99, categoria_id=categoria_eletronicos.id),
            models.Produto(nome="Notebook Dell", preco=2500.00, categoria_id=categoria_eletronicos.id),
            models.Produto(nome="Fone de Ouvido", preco=299.90, categoria_id=categoria_eletronicos.id),
            models.Produto(nome="Camiseta Polo", preco=89.90, categoria_id=categoria_roupas.id),
            models.Produto(nome="Calça Jeans", preco=159.90, categoria_id=categoria_roupas.id),
            models.Produto(nome="Tênis Esportivo", preco=199.90, categoria_id=categoria_roupas.id),
            models.Produto(nome="Python para Iniciantes", preco=49.90, categoria_id=categoria_livros.id),
            models.Produto(nome="Clean Code", preco=79.90, categoria_id=categoria_livros.id),
            models.Produto(nome="Vaso de Planta", preco=35.90, categoria_id=categoria_casa.id),
            models.Produto(nome="Luminária LED", preco=89.90, categoria_id=categoria_casa.id),
        ]
        
        for produto in produtos_exemplo:
            db.add(produto)
        
        db.commit()
        
        print("✅ Banco de dados inicializado com sucesso!")
        print(f"📁 {len(categorias_exemplo)} categorias criadas")
        print(f"📦 {len(produtos_exemplo)} produtos criados")
        
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
