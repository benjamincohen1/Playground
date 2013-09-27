import math,copy, itertools,time
def main():

	#IO

	f = open("UHOIN2.txt")
	tests = int(f.readline())
	#print tests

	for x in range(tests):
		testDetails = f.readline().split()
		testW,testH,numCircles = int(testDetails[0]),int(testDetails[1]),int(testDetails[2])
		circles = []
		#print "New Test.  Room Dim WxH: "+str(testW)+"x"+str(testH)+" Circles: "+str(numCircles)
		for y in range(numCircles):
			l = f.readline().split()
			circles.append((int(l[0]),int(l[1]),int(l[2])))
		#print circles


		cc = canCross(testH,testW,circles)
		#print cc
		tries = 0
		if cc:  #crossed
			print tries
		else:
			done = False
			while done == False:
				rw=rightWallCircles(testH,testW,circles)
				lw=leftWallCircles(testH,testW,circles)

				#print tries+1
				tries +=1
				connections = getConnections(circles)
				tot=0
				if tries==1:
					for x in connections:
						tot+= len(connections[x])
					#print "AVG: "+str(tot/len(circles))
				if numCircles<10:
					mostNeighbors = [c for c in connections if len(connections[c])>-1]

				else:
					mostNeighbors = [c for c in connections if len(connections[c])>(tot/len(circles))*2]
				for x in connections:
					#print x
					pass
					#if len(connections[x])==0:
						#mostNeighbors.append(x)
				#if tries ==1:
					#print "Trying: "+str(len(mostNeighbors))+" neighbors."
				#break
				#print "Generating Subsets:"
				t = time.time()
				combos = list(set(itertools.combinations(mostNeighbors,tries)))
				#print time.time()-t
				#print "Combos: "
				#for x in combos:
					#print "\t"+str(x)
				#print mostNeighbors
				#print "Most popular Neighbors: "+str(len(mostNeighbors))
				#print combos
				#print len(combos)
				subsets = []
				for y in combos:
					#y = [(z[0],z[1],z[2]) for z in y.split(",")]
					#print "Y: "+str(list(y))
					newY=[]
					for x1 in list(y):
						#print x1

						x1=str(x1).split(",")
						newY.append(((int(x1[0].split("(")[1]),int(x1[1][1:]),int(x1[2].split(")")[0]))))


					subsets.append(list(set(circles)-set(newY)))

				if len(subsets)>200:
					subsets = [subs for subs in subsets if subsets.index(subs)%(len(subsets)/100)==0]


				if tries==rightWallCircles(testH,testW,circles):
					print rightWallCircles(testH,testW,circles)
					break
				if tries==leftWallCircles(testH,testW,circles):
					print leftWallCircles(testH,testW,circles)
					break
				if tries == numCircles:
					print numCircles
					break
				#print "Checking "+str(len(subsets))+" Subsets"
				t=time.time()
				for ss in subsets:
					#print ss
					if canCross(testH,testW,list(ss)):
						print tries
						done = True
						break
				#break
				#print time.time()-t

def rightWallCircles(roomH,roomW,circles):
	rightWallCircles=[]
	for c in circles:
		if circleIntersectsRight(roomH,c):
			rightWallCircles.append(c)
	return len(rightWallCircles)
	#print "Right Edge Intersected: "+str(rightEdgeIntersected)
	#print "Circles intersecting: "+str(rightWallCircles)
def leftWallCircles(roomH,roomW,circles):
	leftWallCircles=[]
	for c in circles:
		if circleIntersectsLeft(roomW,roomH,c):
			leftWallCircles.append(c)
	return len(leftWallCircles)
def canCross(roomH,roomW,circles):
	rightEdgeIntersected=False
	leftEdgeIntersected=False
	rightWallCircles=[]
	leftWallCircles=[]
	for c in circles:
		if circleIntersectsRight(roomH,c):
			rightEdgeIntersected=True
			rightWallCircles.append(c)

	#print "Right Edge Intersected: "+str(rightEdgeIntersected)
	#print "Circles intersecting: "+str(rightWallCircles)
	for c in circles:
		if circleIntersectsLeft(roomW,roomH,c):
			leftEdgeIntersected=True
			leftWallCircles.append(c)
	connections=getConnections(circles)
	#print ""
	isPath=True
	loops = 0
	t = time.time()

	#prune circles
	rightNeighbors=[]

	for x in rightWallCircles:
		for y in connections[str(x)]:
			if y not in rightNeighbors:
				rightNeighbors.append(y)
		

	leftNeighbors=[]


	for x in leftWallCircles:
		for y in connections[str(x)]:
			if y not in leftNeighbors:
				leftNeighbors.append(y)
	#end prune

	
	for x in rightNeighbors:
		for y in leftNeighbors:
			loops+=1
			t = time.time()
			b=BFS(x,y,connections)
			t1=time.time()-t
			#if t1>.05:
				#print "DFS: "
				#print t1
			if(b)!=False:
				isPath=False
				break

	#print "Loops: "+str(loops)
	if(isPath):
		#print "There is a path without removing anything"
		return True
	else:
		#remove
		return False
def getConnections(circles):
	connections = {}
	for circle in circles:
		connections[str(circle)]=[]
	for circle in circles:
		circles2=copy.deepcopy(circles)
		circles2.remove(circle)
		for subCircle in circles2:
			c1=circle
			c2=subCircle
			i = IntersectPoints(complex(c1[0],c1[1]),complex(c2[0],c2[1]),c1[2],c2[2])
			#print "\n\n"
			#print str(c1)+str(c2)
			#print i
			#print "\n\n"
			#print(type(i))
			if i!=False and i!=True:
				if subCircle not in connections[str(circle)]:
					connections[str(circle)].append(subCircle)
				if circle not in connections[str(subCircle)]:
					connections[str(subCircle)].append(circle)
	return connections
def BFS(start,end,graph,visited=[]):
	queue=[start]

	visited.append(start)
	while len(queue)>0:
		top=queue.pop(0)
		if top == end:
			return top
		else:
			neighbors = graph[str(top)]
			for x in neighbors:
				if x not in visited:
					visited.append(x)
					queue.append(x)
	return False
def DFS(start,end,graph,discovered=[],explored=[]):
	explored.append(start)
	s = []
	s.append(start)
	while len(s)>0:
		t = s.pop()
		if end == t:
			return t
		neighbors = [n for n in graph[str(t)] if (n not in explored and n not in discovered)]
		if len(neighbors)>0:
			for n in neighbors:
				discovered.append(n)
				s.append(n)
		else:
			explored.append(t)
			if len(s)!=0:
				s.pop()
	return False

def IntersectPoints(P0, P1, r0, r1):
    d = math.sqrt((P1.real - P0.real)**2 + (P1.imag - P0.imag)**2)
    if d > (r0 + r1):
        return False
    elif d < abs(r0 - r1):
        return True
    elif d == 0:
        return True
    else:
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        b = d - a
        h = math.sqrt(r0**2 - a**2)
        P2 = P0 + a * (P1 - P0) / d
        imag1x = P2.real + h * (P1.imag - P0.imag) / d
        imag1y = P2.imag - h * (P1.real - P0.real) / d
        imag2x = P2.real - h * (P1.imag - P0.imag) / d
        imag2y = P2.imag + h * (P1.real - P0.real) / d
        imag1 = complex(imag1x, imag1y)
        imag2 = complex(imag2x, imag2y)
        return [imag1, imag2]


def pointOnCircle(point,circle):
	return (point[0]-circle[0])**2+(point[1]-circle[1])**2==circle[2]**2

def circleIntersectsLine(line,circle):  #make this take two points
	# a=line[0]
	# b=line[1]
	# h=circle[0]
	# k=circle[1]
	r=circle[2]
	x1=0
	x2=100
	y1=line[1]
	y2=line[0]*100 + line[1]
	dx=x2-x1
	dy=y2-y1
	dr=math.sqrt(dx**2 + dy**2)
	d=x1*y2 - x2*y1
	# firstX = (d*dy+sgn(dy)*dx*math.sqrt(r**2*dr**2)-d**2)/(dr**2)
	# secondX = (d*dy-sgn(dy)*dx*math.sqrt(r**2*dr**2)-d**2)/(dr**2)
	# firstY = (-d*dx+abs(dy)*dx*math.sqrt(r**2*dr**2)-d**2)/(dr**2)
	# secondY = (-d*dx-abs(dy)*dx*math.sqrt(r**2*dr**2)-d**2)/(dr**2)
	disc=r**2*dr**2-d**2
	return disc>0
	return ""
def circleIntersectsRight(height,circle):
	r=circle[2]
	x1=0-circle[0]
	x2=0-circle[0]
	y1=0-circle[1]
	y2=height-circle[1]

	dx=x2-x1
	dy=y2-y1
	dr=math.sqrt(dx**2 + dy**2)
	d=x1*y2 - x2*y1
	disc=r**2*dr**2-d**2
	return disc>=0

def circleIntersectsLeft(width,height,circle):
	r=circle[2]
	x1=width-circle[0]
	x2=width-circle[0]
	y1=0-circle[1]
	y2=height-circle[1]

	dx=x2-x1
	dy=y2-y1
	dr=math.sqrt(dx**2 + dy**2)
	d=x1*y2 - x2*y1
	disc=r**2*dr**2-d**2
	return disc>=0
def sgn(n):
	if n<0:
		return -1
	else:
		return 1
main()