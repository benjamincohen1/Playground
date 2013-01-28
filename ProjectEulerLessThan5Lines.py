#print(sum(z for z in range(1000) if z%3==0 or z%5==0))  #problem1 
fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

print(fib(3))
