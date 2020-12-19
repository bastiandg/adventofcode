#!/usr/bin/python3

import re
input = open("day07.txt", "r").read().split("\n")[:-1]

bagRegulations = dict()
bagCheck = "shiny gold"
bagCheckCount = 0


def contentCount(bag):
    contentCountSum = 0
    for key in bagRegulations[bag].keys():
        contentCountSum += bagRegulations[bag][key] + bagRegulations[bag][key] * contentCount(key)
    return contentCountSum


def mustContain(bag, content):
    if content in bagRegulations[bag]:
        return True
    else:
        for b in bagRegulations[bag]:
            if mustContain(b, content):
                return True
    return False


for line in input:
    ruleTokens = line[:-1].replace(" bags", "").replace(" bag", "").split(" contain ")
    id = ruleTokens[0]
    contentTokens = ruleTokens[1].split(", ")
    contents = dict()
    if contentTokens[0] != "no other":
        for contentToken in contentTokens:
            matchObject = re.match(r'^([0-9]+) ([a-z ]+)$', contentToken)
            if matchObject is not None:
                count = int(matchObject.group(1))
                color = matchObject.group(2)
                contents[color] = count
    bagRegulations[id] = contents

for key in bagRegulations.keys():
    if mustContain(key, bagCheck):
        bagCheckCount += 1
print(bagCheckCount)

print(contentCount(bagCheck))
