package main

func bulkSend(numMessages int) float64 {
	messageCost := 0
	for i := 0; i < numMessages; i++ {
		messageCost += 1 + i/100
	}

	return float64(messageCost)
}