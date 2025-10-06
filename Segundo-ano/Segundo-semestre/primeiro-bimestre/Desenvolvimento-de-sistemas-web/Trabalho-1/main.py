from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST - Loja",
    description="API para gerenciamento de produtos e categorias",
    version="1.0.0"
)

# ========== ROTAS PARA CATEGORIAS ==========

@app.get("/categorias/", response_model=List[schemas.Categoria], status_code=status.HTTP_200_OK)
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(models.Categoria).all()
    return categorias

@app.post("/categorias/", response_model=schemas.Categoria, status_code=status.HTTP_201_CREATED)
def criar_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = models.Categoria(nome=categoria.nome)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@app.get("/categorias/{categoria_id}", response_model=schemas.Categoria, status_code=status.HTTP_200_OK)
def buscar_categoria_por_id(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    return categoria

@app.put("/categorias/{categoria_id}", response_model=schemas.Categoria, status_code=status.HTTP_200_OK)
def atualizar_categoria(categoria_id: int, categoria_update: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    
    if categoria_update.nome is not None:
        categoria.nome = categoria_update.nome
    
    db.commit()
    db.refresh(categoria)
    return categoria

@app.delete("/categorias/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    
    produtos_na_categoria = db.query(models.Produto).filter(models.Produto.categoria_id == categoria_id).count()
    if produtos_na_categoria > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Não é possível remover a categoria. Existem {produtos_na_categoria} produto(s) associado(s) a ela."
        )
    
    db.delete(categoria)
    db.commit()
    return None

# ========== ROTAS PARA PRODUTOS ==========

@app.get("/produtos/", response_model=List[schemas.Produto], status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models.Produto).all()
    return produtos

@app.post("/produtos/", response_model=schemas.Produto, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == produto.categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {produto.categoria_id} não encontrada"
        )
    
    db_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco,
        categoria_id=produto.categoria_id
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@app.get("/produtos/{produto_id}", response_model=schemas.Produto, status_code=status.HTTP_200_OK)
def buscar_produto_por_id(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    return produto

@app.put("/produtos/{produto_id}", response_model=schemas.Produto, status_code=status.HTTP_200_OK)
def atualizar_produto(produto_id: int, produto_update: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    
    if produto_update.categoria_id is not None:
        categoria = db.query(models.Categoria).filter(models.Categoria.id == produto_update.categoria_id).first()
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categoria com ID {produto_update.categoria_id} não encontrada"
            )
        produto.categoria_id = produto_update.categoria_id
    
    if produto_update.nome is not None:
        produto.nome = produto_update.nome
    
    if produto_update.preco is not None:
        produto.preco = produto_update.preco
    
    db.commit()
    db.refresh(produto)
    return produto

@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    
    db.delete(produto)
    db.commit()
    return None

@app.get("/produtos/categoria/{categoria_id}", response_model=List[schemas.ProdutoSimples], status_code=status.HTTP_200_OK)
def listar_produtos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    
    produtos = db.query(models.Produto).filter(models.Produto.categoria_id == categoria_id).all()
    return produtos

# ========== ROTA RAIZ ==========

@app.get("/", status_code=status.HTTP_200_OK)
def root(): 
    return {
        "message": "API REST - Loja",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }
