def main():
	command = "LRL"
	debug = False
	squares = 2**len(command)
	stacks = []
	for x in range(squares):
		stacks.append([x+1])
	
	for x in command:
		if x=="L":
			stacks = foldLeft(stacks)
			if debug: 
				print "Folding Left"
				print stacks
		elif x=="R":
			stacks = foldRight(stacks)
			if debug:
				print "Folding Right"
				print stacks

	print stacks[0][::-1]

def foldRight(stacks):
	stacks = stacks[::-1]
	return foldLeft(stacks)[::-1]
		


	return newRH
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
