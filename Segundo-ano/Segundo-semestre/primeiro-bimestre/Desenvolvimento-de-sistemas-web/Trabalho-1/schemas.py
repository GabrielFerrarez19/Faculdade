from pydantic import BaseModel
from typing import Optional, List

class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None

class Categoria(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    categoria_id: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    categoria_id: Optional[int] = None

class Produto(ProdutoBase):
    id: int
    categoria: Categoria
    
    class Config:
        from_attributes = True
    
class ProdutoSimples(BaseModel):
    id: int
    nome: str
    preco: float
    categoria_id: int
    
    class Config:
        from_attributes = True
