package main

import "fmt"

func find_index(numbers []int,target int) []int {
	length:=len(numbers) -1
	var ret[]int
	//for numbers[length]>target {
	//		length--
	//}
	fmt.Println(length)
	lab:
	for j:= length;numbers[j]*2>=target && j>=1;j-- {
		for i:=0;i<j;i++ {
			if numbers[i] + numbers[j] == target {
				ret = append(ret, i+1)
				ret = append(ret, j+1)
				break lab
			}
		}
	}
	return ret
}
func main() {
	var a = []int{-1,0}
	target:= -1
	fmt.Println(find_index(a,target))
}
