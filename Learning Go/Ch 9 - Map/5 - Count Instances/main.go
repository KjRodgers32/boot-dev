package main

func getCounts(messagedUsers []string, vaildUsers map[string]int) {
	for _, user := range messagedUsers {
		if _, ok := vaildUsers[user]; ok {
			vaildUsers[user]++
		}
	}
}
