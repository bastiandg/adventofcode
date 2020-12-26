#!/usr/bin/python3

import regex as re
import copy

input = open("day19.txt", "r").read()[:-1].split("\n\n")
rulesLines = input[0].split("\n")
inputLines = input[1].split("\n")


def isStringList(l):
    for e in l:
        if not isinstance(e, str):
            return False
    return True


def resolveRules(rules):
    resolvedRules = set()
    maxIterations = len(rules)
    c = 0
    while len(resolvedRules) < len(rules) and c < maxIterations:
        for i in range(len(rules)):
            if isinstance(rules[i], str) and i not in resolvedRules:
                for j in range(len(rules)):
                    if not isinstance(rules[j], str):
                        for k in range(len(rules[j])):
                            for l in range(len(rules[j][k])):
                                if rules[j][k][l] == i:
                                    rules[j][k][l] = rules[i]
                            if isStringList(rules[j][k]):
                                rules[j][k] = "".join(rules[j][k])
                        if isStringList(rules[j]):
                            rules[j] = "(" + "|".join(rules[j]) + ")"
                resolvedRules.add(i)
        c += 1
    return rules


rules1 = [None] * len(rulesLines)
for line in rulesLines:
    t = line.split(": ")
    index = int(t[0])
    ruleString = t[1]
    if ruleString[0] == '"':
        rules1[index] = ruleString.replace('"', '')
    else:
        rules1[index] = [[int(i) for i in r.split(" ")] for r in ruleString.split(" | ")]


rules2 = copy.deepcopy(rules1)
rules2[8] = [[42], [42, 8]]
rules2[11] = [[42, 31], [42, 11, 31]]

rules1 = resolveRules(list(rules1))
rules2 = resolveRules(list(rules2))
rules2[8] = rules2[42] + "+"
rules2[11] = "(?P<g11>" + rules2[42] + "(?&g11)*" + rules2[31] + ")"
rules2 = resolveRules(list(rules2))


matchCount = 0
for inputLine in inputLines:
    m = re.match(rules1[0] + "$", inputLine)
    if m is not None:
        matchCount += 1
print(matchCount)

matchCount = 0
for inputLine in inputLines:
    m = re.match(rules2[0] + "$", inputLine)
    if m is not None:
        matchCount += 1
print(matchCount)
