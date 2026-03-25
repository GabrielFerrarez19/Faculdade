package main

import "fmt"

func main() {
	const KmAlcool = 9
	const KmGasolina = 11

	var procoAlcol float32
	var procoGasolina float32

	procoAlcol = 1.5
	procoGasolina = 2.5

	var km float32
	var valorGasolina float32
	var valorAlcool float32

	km = 100
	valorGasolina = km * procoGasolina
	valorAlcool = km * procoAlcol

	fmt.Println("Valor Gasolina: ", valorGasolina)
	fmt.Println("Valor Alcool: ", valorAlcool)

}
