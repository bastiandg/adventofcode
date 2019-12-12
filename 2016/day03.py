#!/usr/bin/env python3

input = open("day03.txt", "r").read().split("\n")[:-1]

possibleTriangles1 = 0
possibleTriangles2 = 0

def possibleTriangle(a, b, c):
	return (a + b) > c

for line in input:
	sides = sorted([int(s) for s in line.split(" ")])
	if possibleTriangle(sides[0], sides[1], sides[2]):
		possibleTriangles1 += 1

triangles = []
for i in range(0, len(input), 3):
	setA = [int(s) for s in input[i].split(" ")]
	setB = [int(s) for s in input[i + 1].split(" ")]
	setC = [int(s) for s in input[i + 2].split(" ")]
	triangles.append(sorted([setA[0], setB[0], setC[0]]))
	triangles.append(sorted([setA[1], setB[1], setC[1]]))
	triangles.append(sorted([setA[2], setB[2], setC[2]]))

for triangle in triangles:
	if possibleTriangle(triangle[0], triangle[1], triangle[2]):
		possibleTriangles2 += 1

print(possibleTriangles1)
print(possibleTriangles2)
