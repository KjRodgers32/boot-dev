package main

import "fmt"

func (e email) cost() int {
	bodyChar := len(e.body)

	if !e.isSubscribed {
		return bodyChar * 5
	} else {
		return bodyChar * 2
	}
}

func (e email) format() string {
	if e.isSubscribed {
		return fmt.Sprintf("'%s' | Subscribed", e.body)
	} else {
		return fmt.Sprintf("'%s' | Not Subscribed", e.body)
	}
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}
