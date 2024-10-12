package main

func calculateFinalBill(costPerMessage float64, numMessages int) float64 {
	discountPercent := calculateDiscountRate(numMessages)
	newCostPerMessage := costPerMessage - (costPerMessage * discountPercent)
	return calculateBaseBill(newCostPerMessage, numMessages)
}

func calculateDiscountRate(messagesSent int) float64 {
	if messagesSent > 5000 {
		return .20
	}
	if messagesSent > 1000 {
		return .10
	} else {
		return 0.0
	}
}

// don't touch below this line

func calculateBaseBill(costPerMessage float64, messagesSent int) float64 {
	return costPerMessage * float64(messagesSent)
}