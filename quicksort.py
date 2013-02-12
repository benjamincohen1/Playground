def qs(l):
	if(len(l)<=1):
		return l
	else:
		pivot=l[0]
		greater=[]
		less=[]
		for x in l[1:]:
			if x>pivot:
				greater.append(x)
			else:
				less.append(x)
		return qs(less)+[pivot]+qs(greater)


print(qs([1,2,3,45,2,1,23,1,512,2,12,312,312,312,3123,12,3,123,534,435,123,12]))



