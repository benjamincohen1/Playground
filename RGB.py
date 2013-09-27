import re
#i = raw_input()
i = "12-13-14,45-156-23,234-234-256"

def convert(x):
	one, two, three = x.split("-")
	print one, two, three
	if int(one) > 255 or int(two) > 255 or int(three) > 255:
		print "INVALID"
		return "INVALID"

	p1 = str(hex(int(str(one)))).split('x')[1]
	p2 = str(hex(int(str(two)))).split("x")[1]
	p3 = str(hex(int(str(three)))).split("x")[1]

	if len(str(p1)) == 1:
		p1 = "0"+p1

	if len(str(p2)) == 1:
		p2 = "0"+p2

	if len(str(p3)) == 1:
		p3 = "0"+p3


	return "#"+p1+p2+p3
things = []
for x in i.split(','):
	x = convert(x)
	things.append(x)

s = ""
for x in things:
	if x == things[-1]:
		s+= x
	else:
		s+= x+", "

print s