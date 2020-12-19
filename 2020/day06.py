#!/usr/bin/python3

input = open("day06.txt", "r").read()[:-1].split("\n\n")

sumAnyoneYes = 0
sumEveryoneYes = 0

for group in input:
    answerAnyoneYes = set()
    for character in group:
        if character != "\n":
            answerAnyoneYes.add(character)
    sumAnyoneYes += len(answerAnyoneYes)

    groupSize = group.count("\n") + 1
    for character in group.split("\n")[0]:
        if group.count(character) == groupSize:
            sumEveryoneYes += 1

print(sumAnyoneYes)
print(sumEveryoneYes)
