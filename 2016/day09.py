#!/usr/bin/env python3

import sys

def recursiveUncompression(length, multiplier, substring):
	index = 0
	decompressedLength = 0
	subCompression = False
	additionalCharacters = 0
	while index < len(substring):
		if substring[index] == "(":
			for j in range(3, 10):
				if (index + j) < len(substring) and substring[index + j] == ")":
					subCompression = True
					compressionInstruction = substring[index + 1:index + j].split("x")
					subLength = int(compressionInstruction[0])
					subMultiplier = int(compressionInstruction[1])
					decompressedLength += recursiveUncompression(subLength, subMultiplier, substring[index + j + 1:index + j + 1 + subLength])
					index = index + j + subLength
					break
		else:
			additionalCharacters += 1
		index += 1
	if subCompression:
		return decompressedLength * multiplier + additionalCharacters
	else:
		return length * multiplier

def iterativeUncompression (input):
	decompressedLength = len(input)
	index = 0

	while index < len(input):
		if input[index] == "(":
			for j in range(3, 10):
				if (index + j) < len(input) and input[index + j] == ")":
					compressionInstruction = input[index + 1:index + j].split("x")
					length = int(compressionInstruction[0])
					multiplier = int(compressionInstruction[1])
					instructionLength = j + 1
					decompressedLength += (multiplier - 1) * length - instructionLength
					index = index + j + length
					break
		index += 1
	return decompressedLength

input = open("day09.txt", "r").read().split("\n")[0]

print(iterativeUncompression(input))
print(recursiveUncompression(1, 1, input))

