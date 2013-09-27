import random, time
def bensApproach(l, newL):
	total = 1
	for i in l:
		total *= i
	for i in l:
		newL.append(total/i)
	#print newL

def harlansApproach(l, length, l1, l2, l3):
	total = 1

	for x in l:
		l1.append(total)
		total *= x
	total = 1
	for x in l[::-1]:
		l2.insert(0,total)
		total *= x


	for x in xrange(length):
		l3.append(l1[x] * l2[x])

	#print l3

l = [random.randint(1,100) for x in range(20000)]
#l = [5,4,1,9]
a = len(l)
t = time.time()
#print l
l1 = [1] * a
l2 = [1] * a
l3 = [1] * a
newL = [1] * a

#print "\n\n\n"
bensApproach(l, newL)
print "Ben's approach took: "+str(time.time() - t)
harlansApproach(l, a, l1, l2, l3)
print "Harlans's approach took: "+str(time.time() - t)
