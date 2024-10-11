package main

import "fmt"

func main() {
	// Older way
	var smsSendingLimit int = 200
	var costPerSms float64 = .85
	var hasPermission bool = true
	var username string = "Kevin Rodgers"

	// Common way
	smsSendingLimitTwo := 200
	costPerSmsTwo := .85
	hasPermissionTwo := true
	usernameTwo := "Kevin Rodgers"

	fmt.Printf("%d %.2f %v %s\n", smsSendingLimit, costPerSms, hasPermission, username)
	fmt.Printf("%d %.2f %v %s", smsSendingLimitTwo, costPerSmsTwo, hasPermissionTwo, usernameTwo)
}