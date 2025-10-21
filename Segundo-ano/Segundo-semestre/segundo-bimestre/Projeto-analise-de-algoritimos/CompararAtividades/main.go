package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	atividades := map[string]string{
		"A1": "17,18",
		"A2": "7,8",
		"A3": "19,21",
		"A4": "2,8",
		"A5": "22,23",
		"A6": "11,12",
		"A7": "5,24",
	}

	var c int

	for i := 1; i < len(atividades); i++ {

		chaveI := "A" + strconv.Itoa(i)

		valoresI := strings.Split(atividades[chaveI], ",")
		inicioI, _ := strconv.Atoi(valoresI[0])
		fimI, _ := strconv.Atoi(valoresI[1])

		for j := 1; j <= len(atividades); j++ {
			if i == j {
				continue
			}
			chaveJ := "A" + strconv.Itoa(j)

			valoresJ := strings.Split(atividades[chaveJ], ",")
			inicioJ, _ := strconv.Atoi(valoresJ[0])
			fimJ, _ := strconv.Atoi(valoresJ[1])

			if fimI < inicioJ || fimJ < inicioI {
				fmt.Printf("A%d (%d-%d) não cruza com A%d (%d-%d)\n", i, inicioI, fimI, j, inicioJ, fimJ)
				c++
			}

		}

	}
	println(c)

}
