#!/usr/bin/python3

input = open("day02.txt", "r").read().split("\n")[:-1]

position = dict({"depth": 0, "distance": 0})
position2 = dict({"depth": 0, "distance": 0})
aim = 0

for line in input:
    direction, lengthString = line.split(" ")
    length = int(lengthString)
    if direction == "forward":
        position["distance"] += length
        position2["distance"] += length
        position2["depth"] += length * aim
    elif direction == "up":
        position["depth"] -= length
        aim -= length
    elif direction == "down":
        position["depth"] += length
        aim += length
    else:
        print(f"error unknow direction ${direction}")
        break
print(position["distance"] * position["depth"])
print(position2["distance"] * position2["depth"])
