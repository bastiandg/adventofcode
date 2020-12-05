#!/usr/bin/python3

input = open("day05.txt", "r").read().split("\n")[:-1]
# input = open("d5", "r").read().split("\n")[:-1]

seatList = []
seatIdList = []

for line in input:
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    seatList.append([row, column])
    seatIdList.append(row * 8 + column)

for n in sorted(seatIdList):
    if (n + 1) not in seatIdList:
        print(n + 1)
        break

print(max(seatIdList))
