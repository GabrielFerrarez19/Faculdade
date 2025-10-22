#!/bin/bash
# Autor: Gabriel Cristiano Ferrarez
# RA: 007311
# Descrição: Lista arquivos executáveis e não vazios em um diretório fornecido

# Verifica se o diretório foi passado como argumento
DIRETORIO="${1:?Erro: Nenhum diretório informado. Uso: $0 <diretório>}"

# Verifica se o caminho é um diretório válido
[[ -d "$DIRETORIO" ]] || { echo "Erro: Diretório '$DIRETORIO' não existe."; exit 1; }

# Usando find para maior velocidade e robustez
contador=0
while IFS= read -r arquivo; do
    echo "$arquivo"
    ((contador++))
done < <(find "$DIRETORIO" -maxdepth 1 -type f -executable -size +0c)

echo "Total de arquivos encontrados: $contador"
