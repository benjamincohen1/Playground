import re,random
def main():
	string1="Ben"
	string2="enb"
	string3="bnnc"
	vals={}
	counts=[]
	count=0
	for val in string1:
		if val not in vals:
			vals[val]=0
	for val in string2:
		if val not in vals:
			vals[val]=1
	for val in string3:
		if val not in vals:
			vals[val]=2
	for x in range(10):
		for x in range(100000):
			vals=shuffle(vals)
			count+=1
			if(evaluate(string1,vals)+evaluate(string2,vals)==evaluate(string3,vals)):
				print("Solution: ")
				print(vals)
				print("This took: "+str(count)+" iterations.")
				counts.append(count)
				count=0
				break
	print("Found "+str(len(counts))+" solutions")
	summ=0
	for x in range(len(counts)):
		summ+=counts[x]
	print("AVG # Iterations = "+str(summ/len(counts)))
def evaluate(string,dic):
	for x in string:
		string=string.replace(x,str(dic[x]))


	return int(string)
def shuffle(dic):
	l=[]
	for x in dic.keys():
		l.append(x)

		random.shuffle(l)
		dic[x]=random.randint(0,9)
	return dic
main()
