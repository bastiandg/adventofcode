#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input = open("day21.txt", "r").read().split("\n")[:-1]
password = [c for c in "abcdefgh"]
scrambled_password = "fbgdceah"


def swap_position(s, n, m):
	s = list(s)
	tmp = s[n]
	s[n] = s[m]
	s[m] = tmp
	return s


def swap_letter(s, c1, c2):
	return swap_position(s, s.index(c1), s.index(c2))


def rotate_right(s, n):
	n = n % len(s)
	return s[-n:] + s[:-n]


def rotate_left(s, n):
	n = n % len(s)
	return s[n:] + s[:n]


def rotate_around_letter(s, c):
	n = s.index(c)
	if n >= 4:
		return rotate_right(s, n + 2)
	else:
		return rotate_right(s, n + 1)


def unrotate_around_letter(s, c):
	n = s.index(c)
	if n % 2 == 1:
		return rotate_left(s, (n + 1) // 2)
	elif n == 2:
		return rotate_right(s, 2)
	elif n == 4:
		return rotate_right(s, 1)
	elif n == 6:
		return s
	elif n == 0:
		return rotate_left(s, 1)


def reverse_slice(s, n, m):
	if n == 0:
		return s[:n] + s[m::-1] + s[m + 1:]
	else:
		return s[:n] + s[m:n - 1:-1] + s[m + 1:]


def move_letter(s, n, m):
	s = list(s)
	tmp = s[n]
	del(s[n])
	s = s[:m] + [tmp] + s[m:]
	return s


def scramble(password, input):
	for line in input:
		tokens = line.split(" ")
		if tokens[0] == "swap" and tokens[1] == "position":
			password = swap_position(password, int(tokens[2]), int(tokens[5]))
		elif tokens[0] == "swap" and tokens[1] == "letter":
			password = swap_letter(password, tokens[2], tokens[5])
		elif tokens[0] == "rotate" and tokens[1] == "right":
			password = rotate_right(password, int(tokens[2]))
		elif tokens[0] == "rotate" and tokens[1] == "left":
			password = rotate_left(password, int(tokens[2]))
		elif tokens[0] == "rotate" and tokens[1] == "based":
			password = rotate_around_letter(password, tokens[6])
		elif tokens[0] == "reverse":
			password = reverse_slice(password, int(tokens[2]), int(tokens[4]))
		elif tokens[0] == "move":
			password = move_letter(password, int(tokens[2]), int(tokens[5]))
	return password


def unscramble(password, input):
	for line in input[::-1]:
		tokens = line.split(" ")
		if tokens[0] == "swap" and tokens[1] == "position":
			password = swap_position(password, int(tokens[2]), int(tokens[5]))
		elif tokens[0] == "swap" and tokens[1] == "letter":
			password = swap_letter(password, tokens[2], tokens[5])
		elif tokens[0] == "rotate" and tokens[1] == "right":
			password = rotate_left(password, int(tokens[2]))
		elif tokens[0] == "rotate" and tokens[1] == "left":
			password = rotate_right(password, int(tokens[2]))
		elif tokens[0] == "rotate" and tokens[1] == "based":
			password = unrotate_around_letter(password, tokens[6])
		elif tokens[0] == "reverse":
			password = reverse_slice(password, int(tokens[2]), int(tokens[4]))
		elif tokens[0] == "move":
			password = move_letter(password, int(tokens[5]), int(tokens[2]))
	return password


p1 = scramble(password, input)
p2 = unscramble(scrambled_password, input)

print("".join(p1))
print("".join(p2))
