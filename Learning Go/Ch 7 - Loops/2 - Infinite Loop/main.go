package main

func maxMessages(thresh int) int {
	var messageCost int
	for i := 0; ; i++ {
		messageCost += 100 + i
		if messageCost > thresh {
			return i
		}
	}
}
