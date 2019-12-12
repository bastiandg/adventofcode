#!/usr/bin/env python3

import math
import string
input = 1364
displaySize = 45
colorSteps = 5
output = [["##"] * displaySize for i in range(displaySize)]
distanceMarker = string.digits + string.ascii_letters
distanceLists = [set()]
distanceLists[0].add((1, 1))
requiredSteps = 0
radius = 50


def coloredPosition(step):
	blue = 200
	if step * colorSteps > 255:
		red = step * colorSteps
		green = 0
	else:
		green = 255 - step * colorSteps
		red = 0
	return "\x1b[38;2;%i;%i;%im#\x1b[0m" % (red, green, blue)

def visited(position):
	global distanceLists
	for distanceList in distanceLists:
		if position in distanceList:
			return True
	return False

def possibleMoves(position):
	x = position[0]
	y = position[1]
	moves = []
	if x > 0 and not isWall(x - 1, y):
		moves.append((x - 1, y))
	if y > 0 and not isWall(x, y - 1):
		moves.append((x, y - 1))
	if not isWall(x, y + 1):
		moves.append((x, y + 1))
	if not isWall(x + 1, y):
		moves.append((x + 1, y))
	return moves

def isWall(x, y):
	n = x * x + 3 * x + 2 * x * y + y + y * y + input
	n2 = n
	onBits = 0
	while n > 0:
		onBits += n % 2
		n = n // 2
	return onBits % 2 == 1

for y in range(displaySize):
	for x in range(displaySize):
		if not isWall(x, y):
			output[y][x] = " " * 2

for step in range(86):
	distanceLists.append(set())
	for field in distanceLists[step]:
		for possibleMove in possibleMoves(field):
			if not visited(possibleMove):
				distanceLists[step + 1].add(possibleMove)
				output[possibleMove[1]][possibleMove[0]] = coloredPosition(step + 1) * 2
				if possibleMove == (31, 39):
					output[possibleMove[1]][possibleMove[0]] = ("\x1b[38;2;%i;%i;%im#\x1b[0m" % (255, 0, 0)) * 2
					requiredSteps = step + 1

reachableLocations = 0
for i in range(radius + 1):
	reachableLocations += len(distanceLists[i])

print("_" * 2 * (displaySize + 1))
for line in output:
	print("|" + "".join(line) + "|")
print("-" * 2 * (displaySize + 1))

print("required steps: %i" % requiredSteps)
print("reachable locations after %i steps: %i" % (radius, reachableLocations))

