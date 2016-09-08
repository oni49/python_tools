string = raw_input("DECRYPT>>")

shift = 0
for c in string:
	print chr(ord(c)-shift),
	shift += 1