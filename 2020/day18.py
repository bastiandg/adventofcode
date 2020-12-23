#!/usr/bin/python3

import re
import sys
input = open("day18.txt", "r").read().split("\n")[:-1]


def evaluateAddPrecedence(expression):
    nested = True
    while nested:
        nested = False
        matches = re.finditer(r"\(([^\(\)]+)\)", expression)
        for match in reversed(list(matches)):
            expression = expression[:match.start(0)] + evaluatePlainAddPrecedence(match.group(0)[1:-1]) + expression[match.end(0):]
            nested = True
    return evaluatePlainAddPrecedence(expression)


def evaluatePlainAddPrecedence(expression):
    nested = True
    while nested:
        nested = False
        matches = re.finditer(r"[0-9]+ \+ [0-9]+", expression)
        matches = list(matches)
        if len(matches) > 0:
            res = str(sum([int(i) for i in matches[0].group(0).split(" + ")]))
            expression = expression[:matches[0].start(0)] + res + expression[matches[0].end(0):]
            nested = True
    return evaluatePlain(expression)


def evaluate(expression):
    nested = True
    while nested:
        nested = False
        matches = re.finditer(r"\(([^\(\)]+)\)", expression)
        for match in reversed(list(matches)):
            expression = expression[:match.start(0)] + evaluatePlain(match.group(0)[1:-1]) + expression[match.end(0):]
            nested = True
    return evaluatePlain(expression)


def evaluatePlain(expression):
    tokens = expression.split(" ")
    ans = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if tokens[i] == "+":
            ans += int(tokens[i + 1])
        elif tokens[i] == "*":
            ans *= int(tokens[i + 1])
        else:
            print("something went wrong")
            sys.exit(1)
    return str(ans)


resultSum = 0
for expression in input:
    result = int(evaluate(expression))
    resultSum += result
print(resultSum)

resultAddRecedence = 0
for expression in input:
    result = int(evaluateAddPrecedence(expression))
    resultAddRecedence += result

print(resultAddRecedence)
