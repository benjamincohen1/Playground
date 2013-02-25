from sets import Set
import copy, itertools
def main():
	n=int(raw_input())
	m=raw_input().split()
	newM=[]
	for x in m:
		newM.append(int(x))
	m=newM
	c=configs(m)
	summ=0
	winners=[]
	for x in c:
		if(nimsum(x) and x not in winners):
			summ+=1
			winners.append(x)
	print(summ)
def configs(m):
	r=[]
	for lst in m:
		rest=copy.copy(m)
		keptSame=lst
		rest.remove(keptSame)
		l=getPermutations(rest)
		for x in l:
			tmp=(list(x))
			tmp.append(keptSame)
			r.append(tmp)
	return r
def getPermutations(lst):
	pileVals=[]
	for x in lst:
		pileVals.append([z for z in range(int(x))])
	z= list((itertools.product(*pileVals)))
	return z
def nimsum(l):
	while 0 in l:
		l.remove(0)
	t=[]
	for x in l:
		z=intToBin(x)
		for d in range(len(z)):
			if(z[d]=="1"):
				t.append(2**d)
	t=sorted(t)
	n = list(Set(t))
	for x in n:
		if(t.count(x)%2!=0):
			return False
	return True
def intToBin(num):
    if(num==0):
        return 0
    else:
        length=len(str(num))
        num_str=str(num)
        s=''
        while(num>1):
            if(num%2==0):
                s='0'+s
                num=num/2
            elif(num%2!=0):
                s='1'+s
                num=((num-1)/2)
        return '1'+s
main()