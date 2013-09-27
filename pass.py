import random
def main():
	random.seed(100)
	for line in open("ff.csv"):
		line2 = line.split(",")
		email = line.split(",")[4]
		p = ""
		for x in range(8):
			r = random.randint(0,3)
			if r == 0 or r == 3:
				c = random.randint(48,57)
			elif r == 1:
				c = random.randint(65,90)
			else:
				c = random.randint(97,122)



			p += chr(c)
		#print "'"+email.lower() +"': '"+ p+"',"
		line2[5] = p
		print line2[:len(line2)-1]
main()