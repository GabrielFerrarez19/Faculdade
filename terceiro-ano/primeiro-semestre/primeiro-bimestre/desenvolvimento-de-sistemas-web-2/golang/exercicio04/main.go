package main

import "fmt"

func main() {
	num := 5

	for i := 1; i <= 10; i++ {
		resultado := num * i
		fmt.Println(resultado)
	}
}
