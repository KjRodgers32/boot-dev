package main

import "fmt"

func main() {
	// Older way
	var smsSendingLimit int = 200
	var costPerSms float64 = .85
	var hasPermission bool = true
	var username string = "Kevin Rodgers"
	const middlename = "Lamont" // constant

	// Common way
	smsSendingLimitTwo := 200
	costPerSmsTwo := .85
	hasPermissionTwo := true
	usernameTwo := "Kevin Rodgers"

	fmt.Printf("%d %.2f %v %s %s\n", smsSendingLimit, costPerSms, hasPermission, username, middlename)
	fmt.Printf("%d %.2f %v %s %s", smsSendingLimitTwo, costPerSmsTwo, hasPermissionTwo, usernameTwo, middlename)
}