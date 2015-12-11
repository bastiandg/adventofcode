#!/usr/bin/python
from PIL import Image
import re

def toggle(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = lights[x][y] ^ 1

def off(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = 0

def on(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = 1

def toggle2(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights2[x][y] += 2

def off2(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if lights2[x][y] > 0:
                lights2[x][y] -= 1

def on2(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights2[x][y] += 1

input = file("day6input", "r").read().split("\n")[:-1]
length = 1000

row = length * [0]
lights = []
lights2 = []
for i in range(length):
    lights.append(list(row))
for i in range(length):
    lights2.append(list(row))

for line in input:
    match = re.match("(turn )?(\w+) (\d+),(\d+) through (\d+),(\d+)", line)
    action = match.group(2)
    x1 = int(match.group(3))
    x2 = int(match.group(5))
    y1 = int(match.group(4))
    y2 = int(match.group(6))
    if action == "off":
        off(x1, x2, y1, y2)
        off2(x1, x2, y1, y2)
    elif action == "on":
        on(x1, x2, y1, y2)
        on2(x1, x2, y1, y2)
    elif action == "toggle":
        toggle(x1, x2, y1, y2)
        toggle2(x1, x2, y1, y2)

offCount = 0
onCount = 0
brightness = 0
pixelList = []
for line in lights:
    for light in line:
        if light == 0:
            pixelList.append((0, 0, 0))
            offCount += 1
        else:
            pixelList.append((255, 255, 255))
            onCount += 1
for line in lights2:
    for light in line:
        brightness += light

image = Image.new("RGB", (1000, 1000))
image.putdata(pixelList)
image.save("/tmp/test.png")

print brightness
