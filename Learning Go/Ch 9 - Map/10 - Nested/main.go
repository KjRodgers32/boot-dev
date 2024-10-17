package main

import "fmt"

func getNameCounts(names []string) map[rune]map[string]int {
	stringMap := make(map[rune]map[string]int)
	for _, name := range names{
		runes := []rune(name)
		if _, ok := stringMap[runes[0]]; !ok {
			stringMap[runes[0]] = map[string]int{name: 1}
		} else {
		stringMap[runes[0]][name]++
		}
	}
	return stringMap
}

func main() {
	stringMap := []string{"billy", "billy", "bob", "joe"}
	fmt.Println(getNameCounts(stringMap))
}