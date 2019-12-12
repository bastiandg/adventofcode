#!/usr/bin/env python3

# inspiration: https://www.redblobgames.com/grids/hexagons/#neighbors-cube
input = open("day11.txt", "r").read()[:-1].split(",")


def move_north(pos):
    return {"x": pos["x"], "y": pos["y"] + 1, "z": pos["z"] - 1}


def move_south(pos):
    return {"x": pos["x"], "y": pos["y"] - 1, "z": pos["z"] + 1}


def move_southeast(pos):
    return {"x": pos["x"] - 1, "y": pos["y"], "z": pos["z"] + 1}


def move_northwest(pos):
    return {"x": pos["x"] + 1, "y": pos["y"], "z": pos["z"] - 1}


def move_southwest(pos):
    return {"x": pos["x"] + 1, "y": pos["y"] - 1, "z": pos["z"]}


def move_northeast(pos):
    return {"x": pos["x"] - 1, "y": pos["y"] + 1, "z": pos["z"]}


def distance(pos):
    return max([abs(pos["x"]), abs(pos["y"]), abs(pos["z"])])


moves = {"n": move_north,
         "s": move_south,
         "sw": move_southwest,
         "nw": move_northwest,
         "se": move_southeast,
         "ne": move_northeast}

max_distance = 0
pos = {"x": 0, "y": 0, "z": 0}

for move in input:
    pos = moves[move](pos)
    if distance(pos) > max_distance:
        max_distance = distance(pos)

print(distance(pos))
print(max_distance)
