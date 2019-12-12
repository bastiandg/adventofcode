#!/usr/bin/env python3

input = "R2 L5 L4 L5 R4 R1 L4 R5 R3 R1 L1 L1 R4 L4 L1 R4 L4 R4 L3 R5 R4 R1 R3 L1 L1 R1 L2 R5 L4 L3 R1 L2 L2 R192 L3 R5 R48 R5 L2 R76 R4 R2 R1 L1 L5 L1 R185 L5 L1 R5 L4 R1 R3 L4 L3 R1 L5 R4 L4 R4 R5 L3 L1 L2 L4 L3 L4 R2 R2 L3 L5 R2 R5 L1 R1 L3 L5 L3 R4 L4 R3 L1 R5 L3 R2 R4 R2 L1 R3 L1 L3 L5 R4 R5 R2 R2 L5 L3 L1 L1 L5 L2 L3 R3 R3 L3 L4 L5 R2 L1 R1 R3 R4 L2 R1 L1 R3 R3 L4 L2 R5 R5 L1 R4 L5 L5 R1 L5 R4 R2 L1 L4 R1 L1 L1 L5 R3 R4 L2 R1 R2 R1 R1 R3 L5 R1 R4"

locations = []
firstCrossing = False

steps = input.split(" ")
direction = 0
# 0 forward
# 1 right
# 2 down
# 3 left

def addLocation (x, y):
    global locations
    global firstCrossing
    if not firstCrossing:
        if [x, y] in locations:
            print("This position was vistied twice x = %i ; y = %i" % (x, y))
            print(abs(y) + abs(x))
            firstCrossing = True
        locations.append([x, y])

x = 0
y = 0

for step in steps:
    locations.append([x, y])
    length = int(step[1:])
    if step[0] == "R":
        direction = (direction + 1 + 4) % 4
    else:
        direction = (direction - 1 + 4) % 4
    if direction == 0:
        for i in range(1, length + 1):
            addLocation(x, y + i)
        y += length
    elif direction == 1:
        for i in range(1, length + 1):
            addLocation(x + i, y)
        x += length
    elif direction == 2:
        for i in range(length, 1, -1):
            addLocation(x, y - i)
        y -= length
    else:
        for i in range(length, 1, -1):
            addLocation(x - i, y)
        x -= length

print("x = %i ; y = %i" % (x, y))
print(abs(y) + abs(x))
