import math,copy, itertools
def main():

	#IO

	tests = int(raw_input())
	#print tests

	for x in range(tests):
		testDetails = raw_input().split()
		testW,testH,numCircles = int(testDetails[0]),int(testDetails[1]),int(testDetails[2])
		circles = []
		#print "New Test.  Room Dim WxH: "+str(testW)+"x"+str(testH)
		for y in range(numCircles):
			l = raw_input().split()
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
				tries +=1
				#remove things
				subsets = list(set(itertools.combinations(circles,len(circles)-tries)))
				#print subsets
				for ss in subsets:
					#print ss
					if canCross(testH,testW,list(ss)):
						print tries
						done = True
						break



	
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
	for x in connections:
		#print str(x)+": "+str(connections[x])
		pass
	#print ""
	isPath=True


	for x in rightWallCircles:
		for y in leftWallCircles:
			b=BFS(x,y,connections)
			if(b)!=False:
				isPath=False
				break

	if(isPath):
		#print "There is a path without removing anything"
		return True
	else:
		#remove
		return False
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

def CompToStr(c):
    return "(" + str(c.real) + ", " + str(c.imag) + ")"

def PairToStr(p):
    return CompToStr(p[0]) + " , " + CompToStr(p[1])

def Test():
    ip = IntersectPoints

    i = ip(complex(0,0), complex(1, 0), 2, 2)
    s = ip(complex(0,0), complex(4, 0), 2, 2)

    print "Intersection:", PairToStr(i)
    print "Wholly inside:", ip(complex(0,0), complex(1, 0), 5, 2)
    print "Single-point edge collision:", PairToStr(s)
    print "No collision:", ip(complex(0,0), complex(5, 0), 2, 2)




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