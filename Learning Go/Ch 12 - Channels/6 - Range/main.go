package main

func concurrentFib(n int) []int {
	intCh := make(chan int)
	values := make([]int, 0)
	go fibonacci(n, intCh)
	for nbr := range intCh {
		values = append(values, nbr)
	}
	return values
}

// don't touch below this line

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		ch <- x
		x, y = y, x+y
	}
	close(ch)
}
