#!/usr/bin/python3

input = open("day08.txt", "r").read().split("\n")[:-1]
# input = open("d8", "r").read().split("\n")[:-1]
programLength = len(input)


def executeProgram(input):
    usedCmds = set()
    acc = 0
    i = 0
    while i not in usedCmds and i != programLength:
        line = input[i].split(" ")
        cmd = line[0]
        value = int(line[1])
        usedCmds.add(i)
        if cmd == "nop":
            i += 1
        elif cmd == "acc":
            acc += value
            i += 1
        elif cmd == "jmp":
            i += value
    return i == programLength, acc


print(executeProgram(input))

for i in range(programLength):
    line = input[i].split(" ")
    cmd = line[0]
    value = int(line[1])
    if cmd != "acc":
        correctedInput = list(input)
        if cmd == "nop":
            correctedInput[i] = f"jmp {value}"
        elif cmd == "jmp":
            correctedInput[i] = f"nop {value}"
        correctExit, acc = executeProgram(correctedInput)
        if correctExit:
            print(acc)
            break
