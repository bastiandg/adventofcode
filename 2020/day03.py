#!/usr/bin/python3

input = open("day03.txt", "r").read().split("\n")[:-1]

lineLength = len(input[0])
treeHitProduct = 1
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

for slope in slopes:
    treeHits = 0
    for i in range(len(input)):
        if i * slope[1] > len(input):
            break
        treeLine = input[i * slope[1]] * ((i * slope[0]) // lineLength + 1)
        if input[i * slope[1]][(i * slope[0]) % lineLength] == "#":
            treeHits = treeHits + 1
    print(f'{slope}: {treeHits}')
    treeHitProduct = treeHitProduct * treeHits

print(treeHitProduct)
