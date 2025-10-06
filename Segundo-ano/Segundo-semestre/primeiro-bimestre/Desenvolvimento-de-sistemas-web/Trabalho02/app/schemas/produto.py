from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.schemas.categoria import CategoriaOut

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    categoria_id: int

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    categoria_id: Optional[int] = None

class ProdutoOut(BaseModel):
    id: int
    nome: str
    preco: float
    categoria_id: int
    categoria: CategoriaOut
    model_config = ConfigDict(from_attributes=True)

class ProdutoSimples(BaseModel):
    id: int
    nome: str
    preco: float
    categoria_id: int
    model_config = ConfigDict(from_attributes=True)

