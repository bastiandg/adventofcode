#!/usr/bin/python3

input = open("day09.txt", "r").read().split("\n")[:-1]
context = 25
previousNumbers = [int(i) for i in input[:context]]
weakNumber = 0
numberList = [int(i) for i in input]

for i in range(context, len(numberList)):
    sumFound = False
    num = numberList[i]
    for j in previousNumbers:
        if (num - j) in previousNumbers and (num / 2) != j:
            sumFound = True
            break
    if not sumFound:
        weakNumber = num
        print(weakNumber)
        break
    previousNumbers[i % context] = num


for i in range(len(numberList)):
    for j in range(i + 1, len(numberList)):
        s = sum(numberList[i:j + 1])
        if s == weakNumber:
            print(numberList[i:j + 1])
            print(min(numberList[i:j + 1]) + max(numberList[i:j + 1]))
        elif s > weakNumber:
            break
