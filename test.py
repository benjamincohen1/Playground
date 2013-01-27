import random
def main():
	d={}
	#z="abcdefghijklmnopqrstuvwxyz"
	z="icrxvapunbtfeogdjwzqkmhlys";  #current winner, 473
	while True:
		s=getSucessors(z)
		b=best(s,z)

		print(b)
		print(str(eval(b)))
		z=b

def eval(cyp):

	leng=0
	abc = "abcdefghijklmnopqrstuvwxyz"
	words = open("enable-6.txt").read().splitlines()
	newabc = cyp
	assert len(newabc) == 26 and set(abc) == set(newabc)
	cipher = dict(zip(abc, newabc))
	for word in words:
	  nword = "".join(map(cipher.get, word))
	  if sorted(nword) == list(nword):
	    leng+=1

	return (leng)
def best(s,curBest):
	curWinner=curBest
	curScore=eval(curBest)
	for x in s:
		if(eval(x)>curScore):
			curScore=eval(x)
			curWinner=x

	return curWinner
def getSucessors(s):
	succesors=[]
	for x in range(100):
		two,three,four,five,six=0,0,0,0,0
		one=random.randint(0,25)
		while(two==one):
			two=random.randint(0,25)
		while(three==one or three==two):
			three=random.randint(0,25)
		while(four==one or four==two or four==three):
			four=random.randint(0,25)
		while(five==one or five==two or five==three or five==four):
			five=random.randint(0,25)
		while(six==one or six==two or six==three or six==four or six ==five):
			six=random.randint(0,25)
		tmp=swapChars(s,one,two,three,four,five,six)
		succesors.append(tmp)
	return succesors
def swapChars(s,one,two,three,four,five,six):
	s=list(s)
	a=[one,two,three,four,five,six]
	random.shuffle(a)
	s[one],s[two],s[three],s[four],s[five],s[six]=s[a[0]],s[a[1]],s[a[2]],s[a[3]],s[a[4]],s[a[5]]
	newS=""

	for x in s:
		newS+=x
	return newS

main()