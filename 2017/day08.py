#!/usr/bin/env python3

input = open("day08.txt", "r").read().split("\n")[:-1]

alltime_max = 0
registers = set()
for line in input:
    line_split = line.split(" ")
    register = line_split[0]
    operator = line_split[1]
    if operator == "dec":
        operator = "-="
    else:
        operator = "+="
    value = line_split[2]
    condition_register = line_split[4]
    conditional = line_split[5]
    condition_value = line_split[6]
    if register not in locals():
        registers.add(register)
        exec("%s = 0" % register)
    if condition_register not in locals():
        registers.add(condition_register)
        exec("%s = 0" % condition_register)

    if eval("%s %s %s" % (condition_register, conditional, condition_value)):
        exec("%s %s %s" % (register, operator, value))
    if globals()[register] > alltime_max:
        alltime_max = globals()[register]

max = 0
for register in registers:
    if globals()[register] > max:
        max = globals()[register]
print(max)
print(alltime_max)
