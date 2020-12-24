#!/usr/bin/python3

input = [15, 12, 0, 14, 3, 1]


def play(input, gameLength):
    indexes = [None] * gameLength
    for i in range(len(input)):
        indexes[input[i]] = (-1, i)
    turn = input[-1]
    for i in range(len(input) - 1, gameLength - 1):
        if indexes[turn][0] == -1:
            turn = 0
        else:
            turn = indexes[turn][1] - indexes[turn][0]
        if indexes[turn] is not None:
            indexes[turn] = (indexes[turn][1], i + 1)
        else:
            indexes[turn] = (-1, i + 1)
    return turn


print(play(input, 2020))
print(play(input, 30000000))
