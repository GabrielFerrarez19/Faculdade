package main

import "fmt"

func main() {
	var altuta float32
	var peso float32
	var imc float32

	altuta = 1.75
	peso = 70

	imc = peso / (altuta * altuta)

	if imc < 25 {
		fmt.Print("Seu peso esta correto")
	} else {
		fmt.Println("Você esta com sobre peso")
	}

	fmt.Println("IMC: ", imc)
}
