#!/usr/bin/env python3

import hashlib
import string
import sys

input = "jlmsuwbz"
otpCount = 74
otpIndex = 63
otpKeys = []
triplets = dict()
quintiplets = dict()
i = 0
part = 1

def hashStretch(s):
	m = hashlib.md5(s.encode())
	for i in range(2016):
		m = hashlib.md5(m.hexdigest().encode())
	return m.hexdigest()

def containedQuintiplet(hash):
	occurence = 100
	quintipletChracter = "z"
	for character in string.hexdigits:
		o = hash.find(character * 5)
		if o >= 0 and o < occurence:
			occurence = o
			quintipletChracter = character
	return quintipletChracter

def containedTriplet(hash):
	occurence = 100
	tripletChracter = "z"
	for character in string.hexdigits:
		o = hash.find(character * 3)
		if o >= 0 and o < occurence:
			occurence = o
			tripletChracter = character
	return tripletChracter

while otpCount > 0:
	value = "%s%i" % (input, i)
	if part == 2:
		hash = hashStretch(value)
	elif part == 1:
		m = hashlib.md5(value.encode())
		hash = m.hexdigest()
	tripletChracter = containedTriplet(hash)
	if tripletChracter != "z":
		if tripletChracter in triplets.keys():
			triplets[tripletChracter].append(i)
		else:
			triplets[tripletChracter] = [i]
	quintipletChracter = containedQuintiplet(hash)
	if quintipletChracter != "z":
		if quintipletChracter in quintiplets.keys():
			quintiplets[quintipletChracter].append(i)
		else:
			quintiplets[quintipletChracter] = [i]
		itList = list(triplets[quintipletChracter])
		for tripletIndex in itList:
			if tripletIndex != i and (tripletIndex + 1000) > i:
				otpKeys.append(tripletIndex)
				triplets[quintipletChracter].remove(tripletIndex)
				if otpCount > 0:
					otpCount -= 1
	i += 1
print(sorted(otpKeys)[otpIndex])

