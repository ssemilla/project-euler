#!/usr/bin/env python

from sets import Set

file = open('p079_keylog.txt')

lines = [l.rstrip() for l in file.readlines()]

lookup = {}

# create the lookup table where key a digit and the value
# is a set containing the digits that follow that digit
for line in lines:
    d = line[0]
    if d in lookup:
        lookup[d].add(line[1])
        lookup[d].add(line[2])
    else:
        lookup[d] = Set([line[1], line[2]])

    d = line[1]
    if d in lookup:
        lookup[d].add(line[2])
    else:
        lookup[d] = Set([line[2]])

# for now let us just assume that there are no duplicate digits
# lets arrange by decending len of the lookup set

passcode = []

while len(lookup) > 1:
    highest = lookup.keys()[0]

    for key in lookup:
        if key != highest:
            if len(lookup[highest]) < len(lookup[key]):
                highest = key

    passcode.append(highest)
    lookup.pop(highest)

last = lookup.keys()[0]
passcode.append(last)
passcode.append(lookup[last].pop())

print "".join(passcode)

