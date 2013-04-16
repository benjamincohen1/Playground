import math
def main():
	f= open("s")
	tests=int(f.readline())
	for z in range(tests):
		line = f.readline()
		line = line.split()

		n=int(line[0])
		m=int(line[1])
		lst=[]
		for x in range(n,m+1):
			if isPalendrome(x) and isPalendrome(floatstrip(x**.5)):
				lst.append(x)
		s=""
		for y in lst:
			s+=str(y)+" "
		print "Case #"+str(z+1)+": "+str(s)

def isPalendrome(n):

	return str(n)==str(n)[::-1]
def floatstrip(x):
    if x == int(x):
        return str(int(x))
    else:
        return str(x)
main()