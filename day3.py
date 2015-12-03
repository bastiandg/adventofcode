#!/usr/bin/python

input = file("day3input", "r").read()

x = 0
y = 0
houses = {(0, 0): 1 }
for movement in input:
    if movement == "^":
        y += 1
    elif movement == "v":
        y -= 1
    elif movement == ">":
        x += 1
    elif movement == "<":
        x -= 1

    if houses.has_key((x, y)):
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

print len(houses)
# for position in houses.keys():
    # print "%i,%i" % (position)


x1 = 0
y1 = 0
x2 = 0
y2 = 0
turn = 0
houses = {(0, 0): 1 }
for movement in input:
    if (turn % 2) == 0:
        x = x1
        y = y1
    else:
        x = x2
        y = y2

    if movement == "^":
        y += 1
    elif movement == "v":
        y -= 1
    elif movement == ">":
        x += 1
    elif movement == "<":
        x -= 1

    if houses.has_key((x, y)):
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

    if (turn % 2) == 0:
        x1 = x
        y1 = y
    else:
        x2 = x
        y2 = y
    turn += 1

print len(houses)
