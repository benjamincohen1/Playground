from nn import *
import sys
def fire():
	n=neuralNet(2,5,1)
	print "Test Data"
	f=10000
	
	datafile = "saveddata.txt"
	n.loadWeightsFromFile(f)

	n=n.updateWeights()
	print "\n\n\n\n"
	fireOnTestData(n,datafile)
		

		   

def fireOnTestData(n,datafile):
	#bolt nut ring scrap
	total = 0

	sse = 0.0
	for line in open(datafile):
		print "line"
		print line
		total+=1
		line = line.strip()
		line = line.split(",")
		#print "Firing on: "+str([float(line[0]),float(line[1]),1])
		outweights = n.fireOnInputValues([float(line[0]),float(line[1]),1])
		

	print outweights

	return sse



def classify(outweights):
	return outweights.index(max(outweights))+1
	
