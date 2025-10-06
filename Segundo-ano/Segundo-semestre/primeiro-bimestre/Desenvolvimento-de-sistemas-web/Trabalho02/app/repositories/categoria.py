from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate

def create(db: Session, payload: CategoriaCreate) -> Categoria:
    objeto = Categoria(**payload.model_dump())
    db.add(objeto)
    db.commit()
    db.refresh(objeto)
    return objeto

def get(db: Session, categoria_id: int) -> Categoria | None:
    return db.get(Categoria, categoria_id)

def get_all(db: Session) -> list[Categoria]:
    return db.query(Categoria).order_by(Categoria.id).all()

def update(db: Session, categoria_id: int, payload: CategoriaUpdate) -> Categoria | None:
    categoria = db.get(Categoria, categoria_id)
    if not categoria:
        return None
    
    if payload.nome is not None:
        categoria.nome = payload.nome
    
    db.commit()
    db.refresh(categoria)
    return categoria

def delete(db: Session, categoria_id: int) -> bool:
    categoria = db.get(Categoria, categoria_id)
    if not categoria:
        return False
    
    # Verificar se existem produtos associados
    from app.models.produto import Produto
    produtos_count = db.query(Produto).filter(Produto.categoria_id == categoria_id).count()
    if produtos_count > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Não é possível remover a categoria. Existem {produtos_count} produto(s) associado(s) a ela."
        )
    
    db.delete(categoria)
    db.commit()
    return True

