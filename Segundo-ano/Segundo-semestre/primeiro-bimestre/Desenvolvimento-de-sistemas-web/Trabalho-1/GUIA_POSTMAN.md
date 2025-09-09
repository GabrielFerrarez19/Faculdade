# 🚀 Guia de Testes com Postman

Este guia mostra como testar a API REST - Loja usando o Postman.

## 📋 Pré-requisitos

1. **Postman instalado** (baixe em: https://www.postman.com/downloads/)
2. **API rodando** (execute: `uvicorn main:app --reload`)
3. **URL base**: `http://localhost:8000`

## 🎯 Configuração Inicial

### 1. Criar uma Collection no Postman

1. Abra o Postman
2. Clique em "New" → "Collection"
3. Nome: "API REST - Loja"
4. Descrição: "Testes da API de produtos e categorias"

### 2. Configurar Variáveis de Ambiente (Opcional)

1. Clique em "Environments" → "New Environment"
2. Nome: "Local Development"
3. Adicione a variável:
   - **Variable**: `base_url`
   - **Initial Value**: `http://localhost:8000`
   - **Current Value**: `http://localhost:8000`

## 📁 Testes para Categorias

### 1. Listar Todas as Categorias

- **Método**: `GET`
- **URL**: `{{base_url}}/categorias/`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

### 2. Criar Nova Categoria

- **Método**: `POST`
- **URL**: `{{base_url}}/categorias/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
    "nome": "Eletrônicos"
  }
  ```

### 3. Buscar Categoria por ID

- **Método**: `GET`
- **URL**: `{{base_url}}/categorias/1`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

### 4. Atualizar Categoria

- **Método**: `PUT`
- **URL**: `{{base_url}}/categorias/1`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
    "nome": "Eletrônicos e Tecnologia"
  }
  ```

### 5. Remover Categoria

- **Método**: `DELETE`
- **URL**: `{{base_url}}/categorias/1`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

## 📦 Testes para Produtos

### 1. Listar Todos os Produtos

- **Método**: `GET`
- **URL**: `{{base_url}}/produtos/`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

### 2. Criar Novo Produto

- **Método**: `POST`
- **URL**: `{{base_url}}/produtos/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
    "nome": "Smartphone iPhone 15",
    "preco": 3999.99,
    "categoria_id": 1
  }
  ```

### 3. Buscar Produto por ID

- **Método**: `GET`
- **URL**: `{{base_url}}/produtos/1`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

### 4. Atualizar Produto

- **Método**: `PUT`
- **URL**: `{{base_url}}/produtos/1`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body** (raw JSON):
  ```json
  {
    "nome": "Smartphone iPhone 15 Pro",
    "preco": 4499.99,
    "categoria_id": 1
  }
  ```

### 5. Remover Produto

- **Método**: `DELETE`
- **URL**: `{{base_url}}/produtos/1`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

### 6. Listar Produtos por Categoria

- **Método**: `GET`
- **URL**: `{{base_url}}/produtos/categoria/1`
- **Headers**: Nenhum necessário
- **Body**: Nenhum

## 🧪 Sequência de Testes Recomendada

### Passo 1: Inicializar Dados (Opcional)

Execute o script para popular o banco:

```bash
python init_db.py
```

### Passo 2: Testar Categorias

1. **Listar categorias** (deve retornar vazio ou dados existentes)
2. **Criar categoria** "Eletrônicos"
3. **Criar categoria** "Roupas"
4. **Listar categorias** (deve mostrar as 2 categorias)
5. **Buscar categoria por ID** (ID 1)
6. **Atualizar categoria** (alterar nome)
7. **Listar categorias** (verificar alteração)

### Passo 3: Testar Produtos

1. **Listar produtos** (deve retornar vazio ou dados existentes)
2. **Criar produto** vinculado à categoria 1
3. **Criar produto** vinculado à categoria 2
4. **Listar produtos** (deve mostrar os 2 produtos)
5. **Buscar produto por ID** (ID 1)
6. **Listar produtos por categoria** (categoria 1)
7. **Atualizar produto** (alterar preço)
8. **Listar produtos** (verificar alteração)

### Passo 4: Testar Relacionamentos

1. **Tentar remover categoria com produtos** (deve retornar erro)
2. **Remover produto**
3. **Remover categoria** (agora deve funcionar)

## 🔍 Verificações Importantes

### Status Codes Esperados

- **200**: Sucesso (GET, PUT)
- **201**: Criado com sucesso (POST)
- **204**: Removido com sucesso (DELETE)
- **404**: Não encontrado
- **400**: Erro de validação

### Respostas de Erro

- **Categoria não encontrada**: `{"detail": "Categoria com ID X não encontrada"}`
- **Produto não encontrado**: `{"detail": "Produto com ID X não encontrado"}`
- **Categoria com produtos**: `{"detail": "Não é possível remover a categoria. Existem X produto(s) associado(s) a ela."}`

## 📊 Exemplos de Respostas

### Categoria Criada

```json
{
  "id": 1,
  "nome": "Eletrônicos"
}
```

### Produto Criado

```json
{
  "id": 1,
  "nome": "Smartphone iPhone 15",
  "preco": 3999.99,
  "categoria_id": 1,
  "categoria": {
    "id": 1,
    "nome": "Eletrônicos"
  }
}
```

### Lista de Produtos por Categoria

```json
[
  {
    "id": 1,
    "nome": "Smartphone iPhone 15",
    "preco": 3999.99,
    "categoria_id": 1
  },
  {
    "id": 2,
    "nome": "Notebook Dell",
    "preco": 2500.0,
    "categoria_id": 1
  }
]
```

## 🚨 Dicas Importantes

1. **Sempre use Content-Type: application/json** para POST e PUT
2. **Verifique os status codes** nas respostas
3. **Teste cenários de erro** (IDs inexistentes, dados inválidos)
4. **Use a documentação automática** em `http://localhost:8000/docs`
5. **Salve as requisições** na collection para reutilizar

## 🔗 Links Úteis

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Rota raiz**: `http://localhost:8000/`
