#!/usr/bin/env python3

import math

input = 368078
square_size = math.ceil(math.sqrt(input))
if square_size % 2 == 0:
    square_size += 1
UP    = {"x":  0, "y": -1}
LEFT  = {"x": -1, "y":  0}
DOWN  = {"x":  0, "y":  1}
RIGHT = {"x":  1, "y":  0}


def build_spirals(square_size, n):
    spiral = [[0 for i in range(square_size)] for j in range(square_size)]
    spiral2 = [[0 for i in range(square_size)] for j in range(square_size)]
    turn = 1
    turn_length = turn
    l = 0
    position = {"x": square_size // 2, "y": square_size // 2}
    spiral2[position["y"]][position["x"]] = 1
    direction = RIGHT
    for i in range(1, square_size * square_size + 1):
        spiral[position["y"]][position["x"]] = i
        adjacent_sum = sum_adjacent(spiral2, position)
        spiral2[position["y"]][position["x"]] = adjacent_sum
        if l == 0 and adjacent_sum > n:
            l = adjacent_sum
        if i == n:
            num_position = dict(position)
        position["x"] += direction["x"]
        position["y"] += direction["y"]
        turn -= 1
        if turn == 0:
            if direction == RIGHT:
                direction = UP
            elif direction == UP:
                direction = LEFT
                turn_length += 1
            elif direction == LEFT:
                direction = DOWN
            elif direction == DOWN:
                direction = RIGHT
                turn_length += 1
            turn = turn_length
    return spiral, spiral2, num_position, l


def print_spiral(spiral, n=-1):
    for line in spiral:
        l = ""
        for number in line:
            if number == n:
                l += '\033[91m%04i \033[0m' % number
            else:
                l += "%04i " % number
        print(l)


def sum_adjacent(spiral, position):
    adjacent_sum = 0
    if position["x"] == 0:
        left_bound = 0
    else:
        left_bound = position["x"] - 1
    if position["y"] > 0:
        adjacent_sum += sum(spiral[position["y"] - 1][left_bound:position["x"] + 2])
    if position["y"] < (len(spiral) - 1):
        adjacent_sum += sum(spiral[position["y"] + 1][left_bound:position["x"] + 2])
    adjacent_sum += sum(spiral[position["y"]][left_bound:position["x"] + 2])
    return adjacent_sum


spiral, spiral2, position, l = build_spirals(square_size, input)
distance = abs(position["x"] - (square_size // 2)) + abs(position["y"] - (square_size // 2))
print("distance: %6i" % distance)
print("sum num:  %6i" % l)
