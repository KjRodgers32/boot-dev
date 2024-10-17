package main

import "fmt"

func bulkSend(numMessages int) float64 {
	var messageCost float64
	for i := 0; i < numMessages; i++ {
		fee := float64(i) / 100.0
		fmt.Println(fee)
		messageCost += 1 + fee
	}
	return float64(messageCost)
}
