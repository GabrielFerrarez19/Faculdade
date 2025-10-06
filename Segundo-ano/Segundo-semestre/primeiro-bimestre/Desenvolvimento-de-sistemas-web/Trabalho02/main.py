from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.rotas import api_rotas

# criar as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="API para gerenciamento de produtos e categorias",
    version="1.0.0"
)

app.include_router(api_rotas)

@app.get("/", status_code=200)
def root():
    return {
        "message": "API REST - Loja",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Configuração para rodar automaticamente no localhost
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",  # localhost
        port=8000,
        reload=True,       # Recarrega automaticamente quando há mudanças
        log_level="info"
    )
