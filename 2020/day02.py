#!/usr/bin/python3

from dataclasses import dataclass
input = open("day02.txt", "r").read().split("\n")[:-1]

@dataclass
class passwordCheck:
    policyMin: int
    policyMax: int
    policyLetter: str
    password: str


passwordCheckList = [None] * len(input)

for i in range(len(input)):
    tokens = input[i].split(" ")
    passwordCheckList[i] = passwordCheck(
        policyMin=int(tokens[0].split("-")[0]),
        policyMax=int(tokens[0].split("-")[1]),
        policyLetter=tokens[1][:-1],
        password=tokens[2]
    )

count1 = 0
count2 = 0
for check in passwordCheckList:
    occurrences = check.password.count(check.policyLetter)
    if occurrences >= check.policyMin and occurrences <= check.policyMax:
        count1 = count1 + 1
    if (check.password[check.policyMin - 1] == check.policyLetter) != \
       (check.password[check.policyMax - 1] == check.policyLetter):
        count2 = count2 + 1
print(count1)
print(count2)
