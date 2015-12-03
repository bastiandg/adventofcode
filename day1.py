#!/usr/bin/python

input = file("day1input", "r").read()

up = "("
down = ")"

endfloor = input.count(up) - input.count(down)

floor = 0
movement = 0
for character in input:
    movement += 1
    if character == up:
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print "movement: %i" % movement
        break
    # print character

print "endfloor: %s" % endfloor
