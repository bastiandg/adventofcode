#!/usr/bin/python3

input = open("day17.txt", "r").read().split("\n")[:-1]


def reset():
    global cycles, cube, startLength, xRange, yRange, zRange, wRange, cycles
    cycles = 6
    cube = set()
    startLength = len(input)
    xRange = [0, startLength + 1]
    yRange = [0, startLength + 1]
    zRange = [0, 1]
    wRange = [0, 1]
    for x in range(startLength):
        for y in range(startLength):
            if input[y][x] == "#":
                cube.add((x, y, 0, 0))


def neighbors(x, y, z, w):
    neighborList = set()
    for xi in range(x - 1, x + 2):
        for yi in range(y - 1, y + 2):
            for zi in range(z - 1, z + 2):
                for wi in range(w - 1, w + 2):
                    neighborList.add((xi, yi, zi, wi))
    neighborList.remove((x, y, z, w))
    return neighborList


def activeNeighbors(cube, x, y, z, w):
    activeNeighborCount = 0
    for neighbor in neighbors(x, y, z, w):
        if neighbor in cube:
            activeNeighborCount += 1
    return activeNeighborCount


reset()

for i in range(cycles):
    previousCube = set(cube)
    xRange = [xRange[0] - 1, xRange[1] + 1]
    yRange = [yRange[0] - 1, yRange[1] + 1]
    zRange = [zRange[0] - 1, zRange[1] + 1]
    print(f"n: {i}")
    for xi in range(*xRange):
        for yi in range(*yRange):
            for zi in range(*zRange):
                coordinate = (xi, yi, zi, 0)
                activeNeighborCount = activeNeighbors(previousCube, *coordinate)
                active = coordinate in previousCube
                if active and activeNeighborCount not in [2, 3]:
                    cube.remove(coordinate)
                elif not active and activeNeighborCount == 3:
                    cube.add(coordinate)
print(len(cube))

reset()

for i in range(cycles):
    previousCube = set(cube)
    xRange = [xRange[0] - 1, xRange[1] + 1]
    yRange = [yRange[0] - 1, yRange[1] + 1]
    zRange = [zRange[0] - 1, zRange[1] + 1]
    wRange = [wRange[0] - 1, wRange[1] + 1]
    print(f"n: {i}")
    for xi in range(*xRange):
        for yi in range(*yRange):
            for zi in range(*zRange):
                for wi in range(*wRange):
                    coordinate = (xi, yi, zi, wi)
                    activeNeighborCount = activeNeighbors(previousCube, *coordinate)
                    active = coordinate in previousCube
                    if active and activeNeighborCount not in [2, 3]:
                        cube.remove(coordinate)
                    elif not active and activeNeighborCount == 3:
                        cube.add(coordinate)
print(len(cube))
