#!/usr/bin/env python3

import hashlib
input = "ojvtpuvg"
password1 = ""
passwordLength1 = 8
password2 = ["g"] * 8
passwordLength2 = 8
i = 0

while passwordLength1 > 0 or passwordLength2 > 0:
	value = "%s%i" % (input, i)
	m = hashlib.md5(value.encode())
	if m.hexdigest()[0:5] == "00000":
		print("%s%i %s" % (input, i, m.hexdigest()))
		print("%s %s" % ("".join(password2), password1))
		if passwordLength1 > 0:
			password1 += m.hexdigest()[5]
			passwordLength1 -= 1
		if passwordLength2 > 0:
			letterIndex = int(m.hexdigest()[5], 16)
			if letterIndex < 8 and password2[letterIndex] == "g":
				password2[letterIndex] = m.hexdigest()[6]
				passwordLength2 -= 1
	i += 1

print(password1)
print("".join(password2))
