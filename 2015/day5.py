#!/usr/bin/python

badCombinationList = ["ab", "cd", "pq", "xy"]

def vowelCount(s):
    if (s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")) >= 3:
        return True
    else:
        return False

def doubleLetter(s):
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

def doubleLetter2(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

def badCombinations(s):
    for badCombination in badCombinationList:
        if s.find(badCombination) > -1:
            return False
    return True

def twoLetterDouble(s):
    for i in range(0, len(s) - 2):
        if s[i+2:].find(s[i:i+2]) > -1:
            return True
    return False

input = file("day5input", "r").read().split("\n")[:-1]

niceCount = 0

for line in input:
    if vowelCount(line) and doubleLetter(line) and badCombinations(line):
        niceCount += 1

print "%i" % niceCount

niceCount = 0

for line in input:
    if doubleLetter2(line) and twoLetterDouble(line):
        niceCount += 1

print "%i" % niceCount
