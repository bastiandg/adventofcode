package main

import (
	"fmt"
	"math"
	"strconv"
)

var steps = []string{"R2", "L5", "L4", "L5", "R4", "R1", "L4", "R5", "R3", "R1", "L1", "L1", "R4", "L4", "L1", "R4", "L4", "R4", "L3", "R5", "R4", "R1", "R3", "L1", "L1", "R1", "L2", "R5", "L4", "L3", "R1", "L2", "L2", "R192", "L3", "R5", "R48", "R5", "L2", "R76", "R4", "R2", "R1", "L1", "L5", "L1", "R185", "L5", "L1", "R5", "L4", "R1", "R3", "L4", "L3", "R1", "L5", "R4", "L4", "R4", "R5", "L3", "L1", "L2", "L4", "L3", "L4", "R2", "R2", "L3", "L5", "R2", "R5", "L1", "R1", "L3", "L5", "L3", "R4", "L4", "R3", "L1", "R5", "L3", "R2", "R4", "R2", "L1", "R3", "L1", "L3", "L5", "R4", "R5", "R2", "R2", "L5", "L3", "L1", "L1", "L5", "L2", "L3", "R3", "R3", "L3", "L4", "L5", "R2", "L1", "R1", "R3", "R4", "L2", "R1", "L1", "R3", "R3", "L4", "L2", "R5", "R5", "L1", "R4", "L5", "L5", "R1", "L5", "R4", "R2", "L1", "L4", "R1", "L1", "L1", "L5", "R3", "R4", "L2", "R1", "R2", "R1", "R1", "R3", "L5", "R1", "R4"}

func main() {
	orientation := 0
	x := 0
	y := 0
	var length int
	for _, step := range steps {
		//fmt.Println(string(step[1:]))
		length, _ = strconv.Atoi(string(step[1:]))
		if string(step[0]) == "R" {
			orientation = (orientation + 1 + 4) % 4
		} else {
			orientation = (orientation - 1 + 4) % 4
		}
		switch orientation {
		case 0:
			y += length
		case 1:
			x += length
		case 2:
			y -= length
		case 3:
			x -= length
		}
	}
	fmt.Println(x, y, math.Abs(float64(x))+math.Abs(float64(y)))
}
