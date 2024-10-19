package main

import (
	"fmt"
)

func waitForDBs(numDBs int, dbChan chan struct{}) {
	for i := 0; i < numDBs; i++ {
		fmt.Println("this is blocking")
		<-dbChan
		fmt.Println("this is done blocking")
	}
}

// don't touch below this line

func getDBsChannel(numDBs int) (chan struct{}, *int) {
	count := 0
	ch := make(chan struct{})

	go func() {
		for i := 0; i < numDBs; i++ {
			ch <- struct{}{}
			fmt.Printf("Database %v is online\n", i+1)
			count++
		}
	}()
	fmt.Println("returning current ch and count")
	return ch, &count
}

func main() {
	dbs := 5
	dbChan, _:= getDBsChannel(dbs)
	waitForDBs(dbs, dbChan)
}