#!/usr/bin/python

import re
import copy

input = file("day7input", "r").read().split("\n")[:-1]

nodes = {}

class Node:
    def __init__(self, operator, operand1, operand2):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        if operator == "->":
            self.value = operand1
        else:
            self.value = None
    def assignment(self):
        if self.operator == "NOT":
            if nodes[self.operand1].value != None:
                self.value = ~ nodes[self.operand1].value
                return True
        elif self.operator == "RSHIFT":
            if nodes[self.operand1].value != None:
                self.value = nodes[self.operand1].value >> self.operand2
                return True
        elif self.operator == "LSHIFT":
            if nodes[self.operand1].value != None:
                self.value = nodes[self.operand1].value << self.operand2
                return True
        elif self.operator == "OR":
            if nodes[self.operand1].value != None and nodes[self.operand2].value != None:
                self.value = nodes[self.operand1].value | nodes[self.operand2].value
                return True
        elif self.operator == "AND":
            if self.operand1 == 1 and nodes[self.operand2].value != None:
                self.value = 1 & nodes[self.operand2].value
                return True
            elif nodes.has_key(self.operand1) and nodes[self.operand1].value != None and nodes[self.operand2].value != None:
                self.value = nodes[self.operand1].value & nodes[self.operand2].value
                return True
        return False

for line in input:
    assignmentMatch = re.match("(\d+) -> (\w+)", line)
    negationMatch = re.match("NOT (\w+) -> (\w+)", line)

    if assignmentMatch:
        nodeName = assignmentMatch.group(2)
        value = int(assignmentMatch.group(1))
        nodes[nodeName] = Node("->", value, None)
    elif negationMatch:
        nodeName = negationMatch.group(2)
        operand1 = negationMatch.group(1)
        nodes[nodeName] = Node("NOT", operand1, None)
    else:
        match = re.match("(\w+) (\w+) (\w+) -> (\w+)", line)
        if match.group(1).isdigit():
            operand1 = int(match.group(1))
        else:
            operand1 = match.group(1)

        if match.group(3).isdigit():
            operand2 = int(match.group(3))
        else:
            operand2 = match.group(3)
        operator = match.group(2)
        nodeName = match.group(4)
        nodes[nodeName] = Node(operator, operand1, operand2)


while not nodes["a"].value:
    for key in nodes.keys():
        if nodes[key].value == None:
            success = nodes[key].assignment()

print nodes["a"].value

