#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dragon(s):
	return s + "0" + invert(s)


def invert(s):
	s = s.replace("1", "a")
	s = s.replace("0", "1")
	s = s.replace("a", "0")
	return s[::-1]

def checksum(s):
	chksum = ""
	for i in range(len(s) // 2):
		if s[i * 2] == s[i * 2 + 1]:
			chksum += "1"
		else:
			chksum += "0"
	if len(chksum) % 2 == 0:
		chksum = checksum(chksum)
	return chksum

def fill(s, length):
	while len(s) < length:
		s = dragon(s)
	print(checksum(s[:length]))

fill("11110010111001001", 272)
fill("11110010111001001", 35651584)
