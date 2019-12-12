#!/usr/bin/env python3


input1 = [106, 118, 236, 1, 130, 0, 235, 254, 59, 205, 2, 87, 129, 25, 255, 118]
input2 = "106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118"

l = list(range(256))


def reverse(l, position, length):
    l = list(l)
    if length < 2:
        return l
    if (position + length) > len(l):
        reversed_section = list(reversed(l[position:] + l[:(position + length) % len(l)]))
    else:
        reversed_section = list(reversed(l[position:position + length]))
    for i in range(length):
        l[(position + i) % len(l)] = reversed_section[i]
    return l


def hash_round(l, input, skip=0, position=0):
    l = list(l)
    for scrambler in input:
        l = reverse(l, position, scrambler)
        position = (position + scrambler + skip) % len(l)
        skip = (skip + 1) % len(l)
    return l, skip, position


def part1(l, input):
    l, _, _ = hash_round(l, input)
    print(l[0] * l[1])


def part2(l, input):
    l = list(l)
    input = [ord(char) for char in input] + [17, 31, 73, 47, 23]
    hash = ""
    position = 0
    skip = 0
    for round in range(64):
        l, skip, position = hash_round(l, input, skip, position)

    for i in range(len(l) // 16):
        block = 0
        for j in range(16):
            block = block ^ l[i * 16 + j]
        hash += format(block, "02x")

    print(hash)


part1(l, input1)
part2(l, input2)
