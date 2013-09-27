def main():
	command = "LT"
	debug = True
	squares = 2**len(command)
	stacks = []
	for x in range(squares):
		curRow = []
		for y in range(squares):
			curRow.append([squares*x+y+1])
		stacks.append(curRow)

	printGrid(stacks)
	

	#return 
	for x in command:
		if x=="L":
			for line in stacks:
				stacks[stacks.index(line)] = foldLeft(line)[len(line)/2-len(command):]
			if debug: 
				print "Folding Left"
				printGrid(stacks)
		elif x=="R":
			for line in stacks:
				stacks[stacks.index(line)] = foldRight(line)[len(line)/2-len(command):]			
			if debug:
				print "Folding Right"
				printGrid(stacks)
		elif x=="D":
			stacks = foldDown(stacks)
		elif x=="U":
			stacks = foldDown(stacks)


	print "\n\n"
	printGrid(stacks[::-1])
def printGrid(g):
	for x in g:
		print x
def foldRight(stacks):
	stacks = stacks[::-1]
	return foldLeft(stacks)[::-1]
		
def foldDown(stacks):
	newstacks = [[] for x in range(len(stacks))]
	print "DOWN"
	for x in range(len(stacks)):
		l = []
		for s in stacks:
			l.append(s[x])
		print l

		newstacks[x] = foldRight(l)

	printGrid(newstacks)
	return newstacks
	#return stacks


def foldUp(stacks):
	stacks = stacks[::-1]
	return foldDown(stacks)[::-1]
		

def foldLeft(stacks):
	rightHalf = stacks[len(stacks)/2:]
	leftHalf = stacks[:len(stacks)/2]
	for x in rightHalf:
		foldStack = leftHalf[len(leftHalf)-rightHalf.index(x)-1]

		for z in foldStack[::-1]:
			x.append(z)
	newRH = []
	for x in rightHalf:
		newRH.append(x)
	return newRH


main()