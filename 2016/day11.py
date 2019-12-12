#!/usr/bin/env python3

import itertools
import sys

# 000
# |||-- position
# ||--- element
# |---- generator / microchip

initialConfiguration = [   0, 100,  10,  20,
			 111, 121,
			  32, 132,  42, 142
		 ]

initialConfiguration2 = [   0, 100,  10,  20, 50, 150, 60, 160,
			 111, 121,
			  32, 132,  42, 142
		 ]

# example from description
# initialConfiguration = [ 100, 110,
			   # 1,
			  # 12
			  # ]

def configuration2int(configuration):
	floorCount = 4
	floorBits = len(configuration)
	separation = int(floorBits / 2) # separation between generator and chip
	configurationIntArray = [0] * 4
	configurationInt = 0
	for item in configuration:
		type = int(item / 100)
		position = item % 10
		element = int((item - type * 100 - position) / 10)
		binItem = (1 << element) << (type * separation)
		configurationIntArray[position] = configurationIntArray[position] | binItem
		configurationInt = configurationInt | (binItem << (position * floorBits))
	return configurationInt


def validConfiguration(configuration):
	for item in configuration:
		if item >= 100:
			position = item % 10
			element = item - 100 - position
			if not (element + position) in configuration:
				for generator in configuration:
					if generator < 100 and (generator % 10) == position:
						return False
	return True

def showConfiguration(configuration, position):
	print("_" * 42)
	for floor in range(3, -1, -1):
		if floor == position:
			floorString = "| >"
		else:
			floorString = "|  "
		for i in range(int(len(configuration) / 2)):
			if (i * 10 + floor) in configuration:
				floorString += "G%i " % i
			else:
				floorString += "   "
		floorString += " | "

		for i in range(int(len(configuration) / 2)):
			if (100 + i * 10 + floor) in configuration:
				floorString += "M%i " % i
			else:
				floorString += "   "
		print("%s|" %floorString)
	print("_" * 42)

def possibleMoves(configuration, position):
	items = []
	for i in range(len(configuration)):
		if configuration[i] % 10 == position:
			items.append(i)
	moves = []
	for combination in itertools.combinations(items, 2):
		if position < 3:
			if validMove(configuration, position, [combination, 1]):
				moves.append([combination, 1])
	for combination in itertools.combinations(items, 1):
		if position > 0:
			if validMove(configuration, position, [combination, -1]):
				moves.append([combination, -1])
		if position < 3:
			if validMove(configuration, position, [combination, 1]):
				moves.append([combination, 1])
	return moves

def finalConfiguration(configuration):
	for i in configuration:
		if i % 10 != 3:
			return False
	return True

def recursiveSolver(configuration, position, depth, moveList):
	global solutions
	global configurationList
	configurationInt = configuration2int(configuration)
	for configurations in configurationList:
		if configurationInt in configurations:
			return False
	if len(configurationList) <= depth:
		configurationList.append(set([configurationInt]))
	else:
		configurationList[depth].add(configurationInt)
	moves = possibleMoves(configuration, position)
	if finalConfiguration(configuration):
		print("solution found steps needed: %i" % depth)
		return True
	else:
		for move in moves:
			if recursiveSolver(movedConfiguration(configuration, position, move), position + move[1], depth + 1, moveList + [move]):
				return True

def movedConfiguration(configuration, position, move):
	items = move[0]
	moveSteps = move[1]
	newConfiguration = list(configuration)
	for item in items:
		newConfiguration[item] += moveSteps
	return newConfiguration

def validMove(configuration, position, move):
	return validConfiguration(movedConfiguration(configuration, position, move))

configurationList = []
recursiveSolver(initialConfiguration, 0, 0, [])

configurationList = []
recursiveSolver(initialConfiguration2, 0, 0, [])
