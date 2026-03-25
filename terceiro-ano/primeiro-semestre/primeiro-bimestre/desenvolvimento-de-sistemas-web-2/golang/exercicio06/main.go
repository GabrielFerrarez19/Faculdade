package main

import "fmt"

func main() {
	n := 20

	a, b := 0, 1

	for i := 0; i < n; i++ {
		fmt.Println(a)
		a, b = b, a+b
	}
}
