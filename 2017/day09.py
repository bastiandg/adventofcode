#!/usr/bin/env python3

import re
input = open("day09.txt", "r").read().split("\n")[:-1][0]

input = re.sub("!.", "", input)

garbage_count = 0
diff = 1
while True:
    length = len(input)
    input = re.sub("<.*?>", "", input, 1)
    diff = length - len(input)
    if diff > 0:
        garbage_count += (diff - 2)
    else:
        break

input = re.sub(",", "", input)

score = 0
depth = 0
for character in input:
    if character == "{":
        depth += 1
        score += depth
    else:
        depth -= 1
print(score)
print(garbage_count)
