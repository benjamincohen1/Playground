import math
def main():
	tests=int(raw_input())
	for x in range(tests):
		printed = False
		prices = {}
		l=int(raw_input())
		c=int(raw_input())
		ns = raw_input().split()
		for n in range(len(ns)):
			for m in range(len(ns)):
				if (int(ns[n])+int(ns[m]))==l and m!=n and printed==False:
					n1=min(n+1,m+1)
					n2=max(n+1,m+1)
					print str(n1)+" "+str(n2)
					printed=True
					break
			if printed:
				break


				
				
def hash(n,l):
	if n<=(l/2.0):
		return n
	else:
		return l-n
main()
