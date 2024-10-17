package main

import (
	"fmt"
	"strings"
)

func removeProfanity(message *string) {
	original_message := *message
	fmt.Printf("%v\n", original_message)
	original_message = strings.ReplaceAll(original_message, "fubb", "****")
	original_message = strings.ReplaceAll(original_message, "shiz", "****")
	original_message = strings.ReplaceAll(original_message, "witch", "*****")
	*message = original_message
}