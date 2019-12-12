#!/usr/bin/env python3

import sys
input = open("day10.txt", "r").read().split("\n")[:-1]

bots = {}

def initialize(commands):
		value = int(commands[1])
		bot = int(commands[5])
		if bot in bots.keys():
			bots[bot] = sorted([value] + bots[bot])
		else:
			bots[bot] = [value]

queue = input
iterations = 0

while len(queue) > 0:
	line = queue.pop(0)
	commands = line.split(" ")
	if commands[0] == "value":
		initialize(commands)
	elif commands[0] == "bot":
		sender = int(commands[1])
		if sender in bots.keys() and len(bots[sender]) == 2:
			if bots[sender] == [17, 61]:
				print(sender)
			if commands[5] == "output":
				receiverLow = - int(commands[6]) -1
			else:
				receiverLow = int(commands[6])
			if commands[10] == "output":
				receiverHigh = - int(commands[11]) -1
			else:
				receiverHigh = int(commands[11])

			if receiverLow in bots.keys():
				bots[receiverLow] = sorted(bots[receiverLow] + [bots[sender][0]])
			else:
				bots[receiverLow] = [bots[sender][0]]

			if receiverHigh in bots.keys():
				bots[receiverHigh] = sorted(bots[receiverHigh] + [bots[sender][1]])
			else:
				bots[receiverHigh] = [bots[sender][1]]
		else:
			queue.append(line)
	iterations += 1

print(bots[-1][0] * bots[-2][0] * bots[-3][0])
