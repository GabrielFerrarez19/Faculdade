package main

import "fmt"

func main() {
	var DESCONTO float32 = 0.1
	var preco float32
	var quantidade int
	var totalDesconto float32
	var total float32

	fmt.Print("Digite o valor:")
	fmt.Scan(&preco)
	fmt.Print("Digite a quantidade:")
	fmt.Scan(&quantidade)

	if quantidade >= 5 {
		total = preco * float32(quantidade)
		totalDesconto = total - (total * DESCONTO)
	} else {
		total = preco * float32(quantidade)
	}

	fmt.Println("Total: ", total)
	fmt.Println("Total com desconto: ", totalDesconto)
}
