package main

import "fmt"

func main() {
	bill := 1850
	jeff := 1650

	var i = 0

	for jeff < bill {
		jeff += 28
		bill += 20
		i++
	}

	fmt.Println("jeff demorara ", i, " anos para alcançar bill")
	fmt.Println("Bill tem ", bill)
	fmt.Println("Jeff tem", jeff)
}
