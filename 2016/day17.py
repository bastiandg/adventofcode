#!/usr/bin/env python3

import hashlib
import string
import sys

def possibleMoves(path, position):
	moves = []
	m = hashlib.md5(path.encode())
	hash = m.hexdigest()[:4]
	if hash[0] in ("b", "c", "d", "e", "f") and position[1] > 0:
		moves.append(True)
	else:
		moves.append(False)
	if hash[1] in ("b", "c", "d", "e", "f") and position[1] < 3:
		moves.append(True)
	else:
		moves.append(False)
	if hash[2] in ("b", "c", "d", "e", "f") and position[0] > 0:
		moves.append(True)
	else:
		moves.append(False)
	if hash[3] in ("b", "c", "d", "e", "f") and position[0] < 3:
		moves.append(True)
	else:
		moves.append(False)
	return moves

states = [[tuple(("bwnlcvfs", (0, 0))),]]
solutions = []
i = 0
while len(states[i]) != 0:
	nextStates = []
	for state in states[i]:
		path = state[0]
		position = state[1]
		if position == (3, 3):
			solutions.append(path)
		else:
			moves = possibleMoves(path, position)
			if moves[0]:
				nextStates.append((path + "U", (position[0], position[1] - 1)))
			if moves[1]:
				nextStates.append((path + "D", (position[0], position[1] + 1)))
			if moves[2]:
				nextStates.append((path + "L", (position[0] - 1, position[1])))
			if moves[3]:
				nextStates.append((path + "R", (position[0] + 1, position[1])))
	states.append(nextStates)
	i += 1
print(solutions[0][8:])
print(len(solutions[-1]) - 8)
