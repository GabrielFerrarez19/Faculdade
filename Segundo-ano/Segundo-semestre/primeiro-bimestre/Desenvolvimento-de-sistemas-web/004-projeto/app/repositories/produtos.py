from sqlalchemy.orm import Session
#tabela produto
from app.models.produto import Produto
#schemas
from app.schemas.produto import ProdutoCreate, ProdutoOut, ProdutoUpdate

#criar produto
def create(db: Session, payload: ProdutoCreate) -> ProdutoOut:
    objeto = Produto(**payload.model_dump())