#!/usr/bin/env python3

input = open("day12.txt", "r").read().split("\n")[:-1]

def isInt(n):
	if n[0] in ('-', '+'):
		return n[1:].isdigit()
	return n.isdigit()

registers = {"a": 0, "b": 0, "c": 1, "d": 0}
i = 0
while i < len(input):
	commands = input[i].split(" ")
	if commands[0] == "cpy":
		if isInt(commands[1]):
			registers[commands[2]] = int(commands[1])
		else:
			registers[commands[2]] = registers[commands[1]]
	elif commands[0] == "inc":
		registers[commands[1]] += 1
	elif commands[0] == "dec":
		registers[commands[1]] -= 1
	elif commands[0] == "jnz":
		jump = True
		if isInt(commands[1]):
			if int(commands[1]) == 0:
				jump = False
		elif registers[commands[1]] == 0:
			jump = False
		if jump:
			if isInt(commands[2]):
				i += int(commands[2]) - 1
			else:
				i += int(registers[commands[2]]) - 1
	i += 1


for register in sorted(registers.keys()):
	print("%s: %i" % (register, registers[register]))
