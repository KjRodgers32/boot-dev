package main

import "errors"

func deleteIfNecessary(users map[string]user, name string) (deleted bool, err error) {
	_, ok := users[name]
	if ok {
		if !users[name].scheduledForDeletion {
			return false, nil
		} else {
			delete(users, name)
			return true, nil
		}
	} else {
		return false, errors.New("not found")
	}
}

type user struct {
	name                 string
	number               int
	scheduledForDeletion bool
}