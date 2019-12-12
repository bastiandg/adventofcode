#!/usr/bin/env python3

import copy
input = open("day08.txt", "r").read().split("\n")[:-1]

display = [[False] * 50 for i in range(6)]

def showDisplay():
	litCount = 0
	print(" " + "_" * 50 + " ")
	for line in display:
		lineString = "|"
		for pixel in line:
			if pixel:
				lineString += "#"
				litCount += 1
			else:
				lineString += " "
		print(lineString + "|")
	print("|" + "_" * 50 + "|")
	print("lit up pixels: %i" % litCount)

def lightUp(length, height):
	for y in range(height):
		for x in range(length):
			display[y][x] = True

def rotateRow(index, rotation):
	global display
	refreshedDisplay = copy.deepcopy(display)
	refreshedDisplay[index] = [False] * 50
	for i in range(len(display[index])):
		refreshedDisplay[index][(i + rotation) % 50] = display[index][i]
	display = refreshedDisplay

def rotateColumn(index, rotation):
	global display
	refreshedDisplay = copy.deepcopy(display)
	for i in range(6):
		refreshedDisplay[(i + rotation) % 6][index] = display[i][index]
	display = refreshedDisplay

for line in input:
	commands = line.split(" ")
	if commands[0] == "rect":
		area = commands[1].split("x")
		length = int(area[0])
		height = int(area[1])
		lightUp(length, height)
	elif commands[0] == "rotate":
		index = int(commands[2].split("=")[1])
		rotation = int(commands[4])
		if commands[1] == "row":
			rotateRow(index, rotation)
		elif commands[1] == "column":
			rotateColumn(index, rotation)
showDisplay()
