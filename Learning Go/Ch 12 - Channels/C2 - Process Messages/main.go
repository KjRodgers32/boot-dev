package main

import "time"

func processMessages(messages []string) []string {
	ch := make(chan string, len(messages))
	processedMessages := make([]string, 0)

	go func() {
		for _, message := range messages {
			ch <- process(message)
		}
		close(ch)
	}()
	
	for msg := range ch {
		processedMessages = append(processedMessages, msg)
	}

	return processedMessages
}


func process(message string) string {
	time.Sleep(time.Second * 1)
	return message + "-processed"
}