package main

import "fmt"

func main() {
	messageLen := 10
	maxMessageLen := 20
	fmt.Println("Trying to send a message of length:", messageLen, "and a max length of:", maxMessageLen)

	if messageLen <= maxMessageLen {
		fmt.Println("Message sent!")
	} else {
		fmt.Println("Message not sent. Max message length exceeded.")
	}

	// if INITIAL_STATEMENT; CONDITION ... limits scope of variable to if statement
	if length := len("sdkfja@jasdfj.com"); length > 1 {
		fmt.Println("Email is valid")
	}
}