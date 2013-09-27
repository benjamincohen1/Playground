def main():
	f=open("c1in2")
	tests=int(f.readline())
	for x in range(tests):
		prices = {}
		l=int(f.readline())
		int(f.readline())
		ns = f.readline().split()
		for n in ns:
			n=int(n)
			if hash(n,l) in prices:
				prices[hash(n,l)]+=1
			else:
				prices[hash(n,l)]=1
		vals=[]
		for x in prices:
			if prices[x]==2:
				for r in range(len(ns)):
					if int(ns[r])==x or int(ns[r])==(l-x):
						vals.append(r)

				print str(min(vals)+1)+" "+str(max(vals)+1)
				break
def hash(n,l):
	if n<=(l/2.0):
		return n
	else:
		return l-n

main()
