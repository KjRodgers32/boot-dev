package main

import (
	"encoding/json"
)

func marshalAll[T any](items []T) ([][]byte, error) {
	byteSlice := make([][]byte,0)
	
	for _, item := range items {
		data, err := json.Marshal(item)
		if err != nil {
			return nil, err
		}
		byteSlice = append(byteSlice, data)
	}

	return byteSlice, nil
}