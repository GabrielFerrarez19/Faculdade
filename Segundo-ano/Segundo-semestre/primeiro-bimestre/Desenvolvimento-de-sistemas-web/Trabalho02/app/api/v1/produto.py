from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.produto import ProdutoCreate, ProdutoUpdate, ProdutoOut, ProdutoSimples
from app.repositories import produto as repo

rotas = APIRouter(prefix="/produtos", tags=["produtos"])

@rotas.post("/", response_model=ProdutoOut, status_code=status.HTTP_201_CREATED)
def criar_produto(payload: ProdutoCreate, db: Session = Depends(get_db)):
    return repo.create(db, payload)

@rotas.get("/", response_model=list[ProdutoOut])
def listar_produtos(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/{produto_id}", response_model=ProdutoOut)
def buscar_produto_por_id(produto_id: int, db: Session = Depends(get_db)):
    produto = repo.get(db, produto_id)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    return produto

@rotas.put("/{produto_id}", response_model=ProdutoOut)
def atualizar_produto(produto_id: int, payload: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = repo.update(db, produto_id, payload)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    return produto

@rotas.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    success = repo.delete(db, produto_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )
    return None

@rotas.get("/categoria/{categoria_id}", response_model=list[ProdutoSimples])
def listar_produtos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return repo.get_by_categoria(db, categoria_id)

