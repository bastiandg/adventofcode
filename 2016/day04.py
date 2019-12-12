#!/usr/bin/env python3

import re
import string
from operator import itemgetter

alphabet = string.ascii_lowercase

input = open("day04.txt", "r").read().split("\n")[:-1]
idSum = 0
storageID = None

for line in input:
	checkSum = re.search("\[([a-z]*)\]", line).group(1)
	id = int(re.search("-([0-9]*)\[", line).group(1))
	line = re.sub("[0-9]*\[[a-z]*\]", "", line)
	occurences = []
	code = ""
	for letter in alphabet:
		occurences.append([line.count(letter), letter])
	letterList = sorted(occurences, key=itemgetter(0), reverse=True)[:5]
	for letter in letterList:
		code += letter[1]
	if code == checkSum:
		idSum += id

	message = ""
	for letter in line:
		if letter == "-":
			message += " "
		else:
			message += alphabet[(alphabet.index(letter) + id) % 26]
	if message.find("northpole") != -1 and message.find("storage") != -1:
		storageID = id

print(idSum)
print(storageID)
