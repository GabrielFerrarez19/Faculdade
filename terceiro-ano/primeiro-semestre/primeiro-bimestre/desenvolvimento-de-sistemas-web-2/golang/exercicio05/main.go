package main

import "fmt"

func main() {
	num := 5
	fatorial := 1

	for i := 1; i <= num; i++ {
		fatorial *= i
	}

	fmt.Println("Fatorial:", fatorial)
}
