def  getIntegerComplement( n):
	n=intToBin(n)
	s=""
	for x in str(n):
		if(x=="1"):
			s+="0"
		else:
			s+="1"
	return binToInt(int(s))



def binToInt(num):
    length=len(str(num))
    num_str=str(num)
    s=0
    for x in range(0,length):
       s=s+(int(num_str[length-1-x])*(2**x))
    return s
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


print(getIntegerComplement(123))