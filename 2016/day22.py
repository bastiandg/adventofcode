#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
input = open("day22.txt", "r").read().split("\n")[2:-1]

disk_array = [[0] * 32] * 30

for line in input:
	tokens = re.match("/dev/grid/node-x(\d*)-y(\d*)\s*(\d*)T\s*(\d*)T\s*(\d*)T\s*(\d*)%", line).groups()
	x = int(tokens[1])
	y = int(tokens[0])
	disk_array[x][y] = dict( {"Size":  int(tokens[2]),
						      "Used":  int(tokens[3]),
						      "Avail": int(tokens[4]),
						      "Perc":  int(tokens[5]),
						      "Loc":   (int(tokens[0]), int(tokens[1]))} )
	print(disk_array[int(tokens[1])][int(tokens[0])])
	# if int(tokens[4]) > 50:
		# print(disk_array[int(tokens[1])][int(tokens[0])])
	# print(disk_array[int(tokens[1])][int(tokens[0])])

for i in range(len(disk_array)):
	for j in range(32):
		print("%i %i %r" % (i, j, disk_array[i][j]))

# print(len(disk_array))
# print(disk_array[26][24])
# print(disk_array[24][26])

fits = 0
for line in disk_array:
	# print(line)
	for disk in line:
		for line2 in disk_array:
			for disk2 in line2:
				# print(disk2)
				# if disk2["Loc"] == (24, 26):
					# print(disk2)
				if disk["Loc"] != disk2["Loc"] and disk["Used"] <= disk2["Avail"]:
					fits += 1

print(fits)
