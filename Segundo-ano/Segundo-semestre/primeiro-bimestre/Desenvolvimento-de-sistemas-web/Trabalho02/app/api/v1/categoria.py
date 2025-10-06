from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate, CategoriaOut
from app.repositories import categoria as repo

rotas = APIRouter(prefix="/categorias", tags=["categorias"])

@rotas.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def criar_categoria(payload: CategoriaCreate, db: Session = Depends(get_db)):
    return repo.create(db, payload)

@rotas.get("/", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/{categoria_id}", response_model=CategoriaOut)
def buscar_categoria_por_id(categoria_id: int, db: Session = Depends(get_db)):
    categoria = repo.get(db, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    return categoria

@rotas.put("/{categoria_id}", response_model=CategoriaOut)
def atualizar_categoria(categoria_id: int, payload: CategoriaUpdate, db: Session = Depends(get_db)):
    categoria = repo.update(db, categoria_id, payload)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    return categoria

@rotas.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_categoria(categoria_id: int, db: Session = Depends(get_db)):
    success = repo.delete(db, categoria_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {categoria_id} não encontrada"
        )
    return None
