import itertools
class bead(object):
	__slots__=['name','color']
	def __init__(self,name,color):
		self.color=color
		self.name=name
	def __str__(self):
		return self.color+" "+self.name
	def __iter__(self):
		return self

	def next(self):
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current - 1

def main():
	numBeads=2
	splitInput=[2,1]
	beads=[]
	for x in range(len(splitInput)):
		for z in range(splitInput[x]):
			beads.append(bead(str(z),"c"+str(x)))
	for y in itertools.permutations(beads):
		for z in y:
			print z
		print("\n")

	
main()