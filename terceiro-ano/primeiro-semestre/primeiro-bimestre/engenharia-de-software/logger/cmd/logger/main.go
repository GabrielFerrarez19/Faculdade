package main

import (
	"fmt"
	"logger/logger"
	"path/filepath"
)

func inicializarConfig() *logger.Logger {
	log := logger.GetInstance()
	log.Info("Inicializando configuração...")
	return log
}

func conectarBanco() *logger.Logger {
	log := logger.GetInstance()
	log.Info("Conectando ao banco de dados...")
	log.Warning("Timeout configurado em 5s")
	return log
}

func processarRequisicao() *logger.Logger {
	log := logger.GetInstance()
	log.Log("Processando requisição")
	log.Error("Falha ao validar token")
	return log
}

func main() {
	fmt.Println("=== Demonstração do Logger (Padrão Singleton) ===")

	log1 := inicializarConfig()
	log2 := conectarBanco()
	log3 := processarRequisicao()

	fmt.Printf("inicializarConfig() -> InstanceID = %d\n", log1.InstanceID())
	fmt.Printf("conectarBanco()    -> InstanceID = %d\n", log2.InstanceID())
	fmt.Printf("processarRequisicao() -> InstanceID = %d\n", log3.InstanceID())
	if log1 == log2 && log2 == log3 {
		fmt.Println("Todas as partes usam o mesmo Logger (Singleton).")
	} else {
		fmt.Println("Erro: instâncias diferentes!")
	}

	fmt.Println("--- Níveis info(), warning(), error() e log() ---")
	log1.Log("Mensagem genérica com Log()")
	log1.Info("Aplicação iniciada")
	log1.Warning("Cache quase cheio")
	log1.Error("Erro de conexão")

	arquivo := filepath.Join(".", "logs.txt")
	if err := log1.SaveToFile(arquivo); err != nil {
		fmt.Printf("Erro ao salvar em arquivo: %v\n", err)
	}

	fmt.Println("\n=== Fim da demonstração ===")
}
