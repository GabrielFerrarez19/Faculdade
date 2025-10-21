package main

import "fmt"

func main() {
    moedas := []int{1, 5, 10, 25, 50, 100}
    valorInserido := 63
    valorRestante := valorInserido
	var sliceMoeda []int

    for i := len(moedas) - 1; i >= 0; i-- {
        fmt.Println("Verificando moeda:", moedas[i])
        for valorRestante >= moedas[i] {
            valorRestante -= moedas[i]
            fmt.Println("Valor restante:", valorRestante)
			sliceMoeda = append(sliceMoeda, moedas[i])
        }
		
		
    }
	fmt.Println("Valor restante:", valorRestante)
	fmt.Println("Moedas",sliceMoeda)

}