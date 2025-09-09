from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    
    # Relacionamento com produtos
    produtos = relationship("Produto", back_populates="categoria")

class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    preco = Column(Float, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    
    # Relacionamento com categoria
    categoria = relationship("Categoria", back_populates="produtos")
