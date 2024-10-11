package main

func getMonthlyPrice(tier string) int {
	price := 0
	switch tier {
	case "basic":
		price = 100
		return price * 100
	case "premium":
		price = 150.00
		return price * 100
	case "enterprise":
		price = 500.00
		return price * 100
	default:
		return price
	}
}