#!/usr/bin/python3

input = open("day03.txt", "r").read().split("\n")[:-1]
inputLength = len(input)
lineLength = len(input[0])

bitCountList = lineLength * [0]

for line in input:
    for i in range(lineLength):
        if line[i] == "1":
            bitCountList[i] += 1

gammaRateString = ""
epsilonRateString = ""

for bitCount in bitCountList:
    if bitCount >= inputLength / 2:
        gammaRateString += "1"
        epsilonRateString += "0"
    else:
        gammaRateString += "0"
        epsilonRateString += "1"

gammaRate = int(gammaRateString, 2)
epsilonRate = int(epsilonRateString, 2)

print(f"gammaRate: {gammaRate}")
print(f"epsilonRate: {epsilonRate}")
print(gammaRate * epsilonRate)
