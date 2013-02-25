import sys
def main():
	sys.setrecursionlimit(10001)
	print(fib2(9990,{}))

	total=0
	for x in range(10000):
		if(fib2(x,{})>=4000000):
			print(total)
			return
		else:
			z=fib2(x,{})
			if(z%2==0):
				total+=z
def fib(n):
	if(n==0 or n==1):
		return n
	else:
		return fib(n-1)+fib(n-2)
def fib2(n,dic):
	if(n in dic):
		return dic[n]
	elif(n==0 or n==1):
		return n
	else:
		x=fib2(n-1,dic)
		dic[n-1]=x
		x2=fib2(n-2,dic)
		dic[n-2]=x2
		return fib2(n-2,dic)+fib2(n-1,dic)

main()
