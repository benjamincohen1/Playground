import random
def main():
	cases = random.randint(1,5)
	print cases
	for x in range(cases):
		w=random.randint(1,100)
		h=random.randint(1,100)
		circles=random.randint(10,20)
		print str(w)+" "+str(h)+" "+str(circles)
		for x in range(circles):
			print str(random.randint(0,w/2))+" "+str(random.randint(0,h/2))+" "+str(random.randint(1,(w*h)/60))


main()