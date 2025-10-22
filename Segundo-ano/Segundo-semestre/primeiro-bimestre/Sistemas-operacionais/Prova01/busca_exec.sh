#!/bin/bash
# Nome: Gabriel Cristiano Ferrarez
# RA: 007311

if [ -z "$1" ]; then
  echo "Erro: Nenhum diretório informado."
  echo"Sintaxe: ./buscar_exec.sh <repositorio>"
  exit 1
fi

DIRETORIO="$1"


if [ ! -d "$DIRETORIO" ]; then
  echo "Erro: Diretório '$DIRETORIO' não existe."
  exit 1
fi


contador=0


for arquivo in "$DIRETORIO"/*; do
  if [ -f "$arquivo" ] && [ -x "$arquivo" ] && [ -s "$arquivo" ]; then
    echo "$arquivo"
    contador=$((contador + 1))
  fi
done

echo "Total de arquivos encontrados: $contador"

