import re
def main():
	#let's backtrace!
	s1="ben"
	s2="coh"
	s3="air"
	print(replace("123"))
def replace(string):
	returns=[]
	try:
		return int(string)

	except:
		for x in string:
			try:
				int(x)
			except:
				for z in range(0,10):
					returns.append(string.replace(x,str(z)))
				return returns			

main()
