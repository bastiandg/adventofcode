#!/usr/bin/python

import re
input = file("day8input", "r").read().split("\n")[:-1]

lengthDifference = 0
for line in input:
    totalLength = len(line)
    strippedLine = line
    strippedLine = re.sub(r'\\x[0-9a-f][0-9a-f]', "x", strippedLine)
    strippedLine = re.sub("^\"", "", strippedLine)
    strippedLine = re.sub("\"$", "", strippedLine)
    strippedLine = strippedLine.replace("\\\\", "\\")
    strippedLine = strippedLine.replace("\\\"", "\"")
    strippedLength = len(strippedLine)
    print "%s %i" % (line, len(line))
    print "%s %i" % (strippedLine, len(strippedLine))
    lengthDifference += totalLength - strippedLength
print lengthDifference
