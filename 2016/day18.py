#!/usr/bin/env python3

import sys

input = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."
safeCount = input.count(".")

l = len(input)
rowCount = 400000
rows = [[x == "^" for x in input],]

for i in range(rowCount - 1):
	newRow = [True] * l
	for j in range(len(input)):
		trap = False
		if j == 0:
			if rows[i][j + 1]:
				trap = True
		elif j == l - 1:
			if rows[i][j - 1]:
				trap = True
		else:
			if   rows[i][j - 1] != rows[i][j + 1]:
				trap = True
		if not trap:
			safeCount += 1
			newRow[j] = False
	rows.append(newRow)
print(safeCount)

