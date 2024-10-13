package main

import (
	"fmt"
	"time"
)

type birthdayMessage struct {
	birthdayTime time.Time
	recipientName string
}

type sendingReport struct {
	reportName string
	numbersOfSends int
}

type message interface {
	getMessage() string
}

func sendMessage(msg message) (string, int) {
	cost := len(msg.getMessage()) * 3
	return msg.getMessage(), cost
}

func (bm birthdayMessage) getMessage() string {
	return fmt.Sprintf("Hi %s, it is your birthday on %s", bm.recipientName, bm.birthdayTime.Format(time.RFC3339))
}

func (sr sendingReport) getMessage() string {
	return fmt.Sprintf(`Your "%s" report is ready. You've sent %v messages.`, sr.reportName, sr.numbersOfSends)
}