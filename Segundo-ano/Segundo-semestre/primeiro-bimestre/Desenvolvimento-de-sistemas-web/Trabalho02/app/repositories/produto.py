from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.produto import Produto
from app.models.categoria import Categoria
from app.schemas.produto import ProdutoCreate, ProdutoUpdate

def create(db: Session, payload: ProdutoCreate) -> Produto:
    # Verificar se categoria existe
    categoria = db.get(Categoria, payload.categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {payload.categoria_id} não encontrada"
        )
    
    objeto = Produto(**payload.model_dump())
    db.add(objeto)
    db.commit()
    db.refresh(objeto)
    return objeto

def get(db: Session, produto_id: int) -> Produto | None:
    return db.get(Produto, produto_id)

def get_all(db: Session) -> list[Produto]:
    return db.query(Produto).order_by(Produto.id).all()

def get_by_categoria(db: Session, categoria_id: int) -> list[Produto]:
    # Verificar se categoria existe
    categoria = db.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    
    return db.query(Produto).filter(Produto.categoria_id == categoria_id).all()

def update(db: Session, produto_id: int, payload: ProdutoUpdate) -> Produto | None:
    produto = db.get(Produto, produto_id)
    if not produto:
        return None
    
    # Verificar categoria se fornecida
    if payload.categoria_id is not None:
        categoria = db.get(Categoria, payload.categoria_id)
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categoria com ID {payload.categoria_id} não encontrada"
            )
        produto.categoria_id = payload.categoria_id
    
    if payload.nome is not None:
        produto.nome = payload.nome
    
    if payload.preco is not None:
        produto.preco = payload.preco
    
    db.commit()
    db.refresh(produto)
    return produto

def delete(db: Session, produto_id: int) -> bool:
    produto = db.get(Produto, produto_id)
    if not produto:
        return False
    
    db.delete(produto)
    db.commit()
    return True
