#!/usr/bin/env python3
"""
Script para executar a API REST - Loja
Este script facilita a execução da aplicação no localhost
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Iniciando API REST - Loja...")
    print("📍 URL: http://localhost:8000")
    print("📚 Documentação: http://localhost:8000/docs")
    print("🔄 Pressione Ctrl+C para parar o servidor")
    print("-" * 50)
    
    uvicorn.run(
        app,
        host="127.0.0.1",  # localhost
        port=8000,
        reload=True,       # Recarrega automaticamente quando há mudanças
        log_level="info"
    )

