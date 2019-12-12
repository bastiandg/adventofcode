#!/usr/bin/env python3

import re
import sys

input = open("day07.txt", "r").read().split("\n")[:-1]

def containsAbba (s):
	if len(s) < 4:
		return False
	for i in range(len(s) - 3):
		if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
			return True

def findAba(s):
	babList = []
	for i in range(len(s) - 2):
		if s[i] == s[i + 2] and s[i] != s[i + 1]:
			babList.append("%s%s%s" %(s[i + 1], s[i], s[i + 1]))
	return babList

def containsBab(s, babList):
	for aba in babList:
		if s.find(aba) > -1:
			return True

tlsCount = 0
sslCount = 0
for line in input:
	ipAbba = False
	hyperAbba = False
	babList = []

	hyperPattern = re.compile('\[.*?\]')
	hyperSequences = [ match[1:-1] for match in hyperPattern.findall(line) ]
	ipSequences = re.sub("\[[a-z]*\]", " ", line).split(" ")

	for ipSequence in ipSequences:
		if containsAbba(ipSequence):
			ipAbba = True
			break
	if ipAbba:
		for hyperSequence in hyperSequences:
			if containsAbba(hyperSequence):
				hyperAbba = True
				break
		if not hyperAbba:
			tlsCount += 1

	for ipSequence in ipSequences:
		babList += findAba(ipSequence)
	for hyperSequence in hyperSequences:
		if containsBab(hyperSequence, babList):
			sslCount += 1
			break

print("TLS count: %i" % tlsCount)
print("SSL count: %i" % sslCount)
