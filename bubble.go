package main

import (
	"fmt"
) //to Println

//to run Enter "go run 'filename.go'"

func main() {
	a := []int{1, 4, 14, 1245, 1, 5, 5, 15, 1, 51, 5, 235, 7347, 51, 5, 2}
	N := len(a) // число элементов в списке

	for i := 0; i < N-1; i++ { // N-1 итераций работы алгоритма
		for j := 0; j < N-1-i; j++ { // проход по оставшимся не отсортированным парам массива
			if a[j] > a[j+1] {
				a[j], a[j+1] = a[j+1], a[j]
			}
		}
	}

	fmt.Println(a)
}
