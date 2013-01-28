def getSum(string):
    x=0
    for z in string:
        x+=int(z)
    return x

def getEqualSumSubstring (s):

    if(len(s)==0 or len(s)==1):
        return 0
    for x in range(len(str(s)),1,-1):
        strings=getStringsOfLen(s,x)
        for s in strings:
            one=s[:-len(s)/2]
            two=s[len(s)/2:]
            if(getSum(one)==getSum(two) and len(one)==len(two)):
                return x
    return 0

def getStringsOfLen(string,num):
    if(len(string)==num):
        return [string]
    else:
        r=[]
        offset=0
        for x in range(len(string)-num+1):
            r.append(string[offset:offset+num])
            offset+=1
    return r


print(getEqualSumSubstring("986561517416921217551395112859219257312"))