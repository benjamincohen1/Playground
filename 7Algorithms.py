def interest(prin,rate,period,duration):
	return prin*((1+rate/period)**(period*duration))

def balance():
	pass

print(interest(10000000,.05,4,5))