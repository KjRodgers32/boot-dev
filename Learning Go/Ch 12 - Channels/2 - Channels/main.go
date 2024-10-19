package main

import (
	"fmt"
	"time"
)

type email struct {
	body string
	date time.Time
}

func checkEmailAge(emails [3]email) [3]bool {
	isOldChan := make(chan bool)

	go sendIsOld(isOldChan, emails)

	isOld := [3]bool{}
	isOld[0] = <-isOldChan
	fmt.Println(isOld[0])
	isOld[1] = <-isOldChan
	fmt.Println(isOld[1])
	isOld[2] = <-isOldChan
	fmt.Println(isOld[2])
	return isOld
}

// don't touch below this line

func sendIsOld(isOldChan chan<- bool, emails [3]email) {
	for _, e := range emails {
		if e.date.Before(time.Date(2020, 0, 0, 0, 0, 0, 0, time.UTC)) {
			fmt.Println("This shit is true")
			isOldChan <- true
			continue
		}
		fmt.Println("This is false for sure")
		isOldChan <- false
	}
}

func main() {
	emails := [3]email{
	{
		body: "I have stolen princesses back from sleeping barrow kings.",
		date: time.Date(2019, 0, 0, 0, 0, 0, 0, time.UTC),
	},
	{
		body: "I burned down the town of Trebon",
		date: time.Date(2019, 6, 6, 0, 0, 0, 0, time.UTC),
	},
	{
		body: "I have spent the night with Felurian and left with both my sanity and my life.",
		date: time.Date(2008, 7, 0, 0, 0, 0, 0, time.UTC),
	},
}
	checkEmailAge(emails)
}