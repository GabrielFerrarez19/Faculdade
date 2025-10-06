from pydantic import BaseModel, ConfigDict
from typing import Optional

class CategoriaCreate(BaseModel):
    nome: str

class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None

class CategoriaOut(BaseModel):
    id: int
    nome: str
    model_config = ConfigDict(from_attributes=True)

