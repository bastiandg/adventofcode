#!/usr/bin/python3

input = open("day16.txt", "r").read()[:-1].split("\n\n")

validityRanges = dict()
errorRate = 0
columnCount = (input[0].count("\n") + 1)
columns = [set() for i in range(columnCount)]
columnCandidates = dict()
columnOrder = [""] * columnCount


def inAnyRange(n):
    for r in validityRanges.values():
        if n in r[0] or n in r[1]:
            return True
    return False


# validity ranges
for line in input[0].split("\n"):
    lineTokens = line.split(": ")
    fieldName = lineTokens[0]
    valueTokens = lineTokens[1].split(" ")
    rangeTokens1 = valueTokens[0].split("-")
    rangeTokens2 = valueTokens[2].split("-")
    validityRanges[fieldName] = (range(int(rangeTokens1[0]), int(rangeTokens1[1]) + 1), range(int(rangeTokens2[0]), int(rangeTokens2[1]) + 1))

# ticket value check and column creation
for ticket in input[2].replace("nearby tickets:\n", "").split("\n"):
    ticketValues = [int(i) for i in ticket.split(",")]
    validTicket = True
    for i in range(columnCount):
        if not inAnyRange(ticketValues[i]):
            errorRate += ticketValues[i]
            validTicket = False
    if validTicket:
        for i in range(columnCount):
            columns[i].add(ticketValues[i])

# column candidate determination
for fieldName in validityRanges.keys():
    candidates = []
    for i in range(columnCount):
        allValuesValid = True
        for value in columns[i]:
            if value not in validityRanges[fieldName][0] and value not in validityRanges[fieldName][1]:
                allValuesValid = False
                break
        if allValuesValid:
            candidates.append(i)
    columnCandidates[fieldName] = candidates

# my ticket
myTicket = [int(i) for i in input[1].split("\n")[1].split(",")]

# column name determination
while "" in columnOrder:
    for fieldName in columnCandidates.keys():
        if len(columnCandidates[fieldName]) == 1:
            index = columnCandidates[fieldName][0]
            columnOrder[index] = fieldName
            for f in columnCandidates.keys():
                if index in columnCandidates[f]:
                    columnCandidates[f].remove(index)

ticketChecksum = 1
for i in range(columnCount):
    if columnOrder[i].startswith("departure"):
        ticketChecksum *= myTicket[i]

print(ticketChecksum)
print(errorRate)
