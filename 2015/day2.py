#!/usr/bin/python

input = file("day2input", "r").read().split("\n")[:-1]

papersum = 0
ribbonsum = 0
for present in input:
    l, w, h = tuple(present.split("x"))
    l = int(l)
    w = int(w)
    h = int(h)
    side1 = l * w
    side2 = l * h
    side3 = w * h
    area = 2 * side1  + 2 * side2 + 2 * side3 + min(side1, side2, side3)
    volume = l * w * h
    ribbon = 2 * l + 2 * h + 2 * w - 2 * max(l, h, w) + volume
    ribbonsum += ribbon
    papersum += area

print papersum
print ribbonsum

