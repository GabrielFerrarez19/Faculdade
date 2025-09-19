from sqlalchemy.orm import Session
#tabela produto
from app.models.produto import Produto
#schemas
from app.schemas.produto import ProdutoCreate, ProdutoOut, ProdutoUpdate

#criar produto
def create(db: Session, produto: ProdutoCreate):