#!/usr/bin/python3

input = open("day01.txt", "r").read().split("\n")[:-1]
requirementSum = 0
extendedRequirementSum = 0


def extendedFuelRequirement(mass):
    t = mass // 3 - 2
    sum = t
    while t > 0:
        t = t // 3 - 2
        if t > 0:
            sum += t
    return sum


for line in input:
    mass = int(line)
    requirementSum += mass // 3 - 2
    extendedRequirementSum += extendedFuelRequirement(mass)

print(requirementSum)
print(extendedRequirementSum)
