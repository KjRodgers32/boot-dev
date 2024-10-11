package main

import "fmt"

func concat(s1 string, s2 string) string {
	return s1 + s2
}

func main() {
	firstName := "Kevin"
	lastName := " Rodgers"

	fmt.Println(concat(firstName, lastName))
}