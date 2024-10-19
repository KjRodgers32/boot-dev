package main

import (
	"fmt"
	"time"
)

func waitForDBs(numDBs int, dbChan chan struct{}) {
	<-dbChan
	numDBs--
	time.Sleep(time.Millisecond * 2)
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

	return ch, &count
}
