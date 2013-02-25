inp=raw_input()
inp=int(inp)
if inp > 300:
	z=(inp-300)*80 + 20000
elif inp>100:
	z=(inp-100)*70 + 6000
else:
	z=(inp)*60

print z
