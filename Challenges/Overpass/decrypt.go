package main

import (
	"fmt"
	"os"
)

func rot47(input string) string {
	result := make([]byte, len(input))
	for i := 0; i < len(input); i++ {
		c := input[i]

		if c >= 33 && c <= 126 {
			result[i] = byte(33 + ((int(c)-33+47)%94))
		} else {
			result[i] = c
		}
	}
	return string(result)
}

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s <file.overpass>\n", os.Args[0])
		os.Exit(1)
	}
	data, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	fmt.Println(rot47(string(data)))
}