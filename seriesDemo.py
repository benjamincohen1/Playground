def main():
	x=input()

	l=[2.0/(2**z) for z in range(x)]
	print l

	summ=0
	for n in l:
		summ+=n
	print "The sum of the series is: "+str(summ)

main()
