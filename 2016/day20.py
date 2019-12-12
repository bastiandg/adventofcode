#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input = open("day20.txt", "r").read().split("\n")[:-1]

minList = []
maxList = []
rangeList = []
freeRangeList = []

for line in input:
	l = line.split("-")
	minList.append(int(l[0]))
	maxList.append(int(l[1]))
	rangeList.append(range(int(l[0]), int(l[1]) + 1))

maxList = sorted(maxList)
minList = sorted(minList)

candidateList = []
for candidate in maxList:
	blocked = False
	for r in rangeList:
		if (candidate + 1) in r:
			blocked = True
			break
	if not blocked:
		candidateList.append(candidate + 1)
		for min in minList:
			if (candidate + 1) < min:
				freeRangeList.append(range(candidate + 1, min))
				break

freeIPCount = 0
for freeRange in freeRangeList:
	freeIPCount += len(freeRange)

print(candidateList[0])
print(freeIPCount)
