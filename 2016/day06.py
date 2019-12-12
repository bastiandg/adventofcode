#!/usr/bin/env python3

import re
import string
from operator import itemgetter

alphabet = string.ascii_lowercase
input = open("day06.txt", "r").read().split("\n")[:-1]
counter = [[0] * 26 for i in range(8)]
message1 = ""
message2 = ""

for line in input:
	for i in range(len(line)):
		counter[i][alphabet.index(line[i])] += 1

for position in counter:
	message1 += alphabet[position.index(sorted(position, reverse=True)[0])]
	message2 += alphabet[position.index(sorted(position)[0])]

print(message1)
print(message2)
