#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# discs = [[5, 4],
	 # [2, 1]]

discs = [[13,  1],
	 [19, 10],
	 [ 3,  2],
	 [ 7,  1],
	 [ 5,  3],
	 [17,  5],
	 [11,  0]]

pointer = "̣̣↓"

def printDiscs():
	for disc in discs:
		print("-" * disc[1] + pointer + "-" * (disc[0] - disc[1] - 1) + "|" )

def forward():
	for i in range(len(discs)):
		discs[i][1] = (discs[i][1] + 1) % discs[i][0]

def releasePosition():
	for i in range(len(discs)):
		if (discs[i][1] + i + 1) != discs[i][0]:
			return False
	return True

i = 0
while not releasePosition():
	forward()
	i += 1
print(i)
