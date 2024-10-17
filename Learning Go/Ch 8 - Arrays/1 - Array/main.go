package main

func getMessageWithRetries(primary, secondary, tertiary string) ([3]string, [3]int) {
	messageArray := [3]string{primary, secondary, tertiary}
	costArray := [3]int{len(primary), len(primary) + len(secondary), len(primary) + len(secondary) + len(tertiary)}
	return messageArray, costArray
}

