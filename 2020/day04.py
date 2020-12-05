#!/usr/bin/python3

import regex as re
input = open("day04.txt", "r").read()[:-1].split("\n\n")

mandatoryFields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


def hgtValid(hgt):
    try:
        n = int(hgt[:-2])
    except ValueError:
        return False
    if hgt[-2:] == "in" and n <= 76 and n >= 59:
        return True
    elif hgt[-2:] == "cm" and n <= 193 and n >= 150:
        return True
    return False


validPassports1 = 0
validPassports2 = 0

for line in input:
    line = line.replace("\n", " ")
    valid = True
    for field in mandatoryFields:
        if f'{field}:' not in line:
            valid = False
            break
    if valid:
        validPassports1 += 1
        fields = line.split(" ")
        for field in fields:
            key = field[:3]
            value = field[4:]
            if key == "hgt" and not hgtValid(value):
                valid = False
                break
            elif key == "byr" and int(value) not in range(1920, 2003):
                valid = False
                break
            elif key == "iyr" and int(value) not in range(2010, 2021):
                valid = False
                break
            elif key == "eyr" and int(value) not in range(2020, 2031):
                valid = False
                break
            elif key == "hcl" and not re.match('#[0-9a-f]{6}', value):
                valid = False
                break
            elif key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
                break
            elif key == "pid" and not re.match('[0-9]{9}$', value):
                valid = False
                break
        if valid:
            validPassports2 += 1

print(validPassports1)
print(validPassports2)
