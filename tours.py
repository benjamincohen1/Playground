import sys
def main():
	if(len(sys.argv)!=3):
		print("Incorrect Number of arguements.  Usage: python tours.py x y")
		return 
	m=int(sys.argv[1])
	n=int(sys.argv[2])
	count=paths(0,0,m,n)
	print(count)
def paths(x,y,N,M):
	visited={}
	for x1 in range(N):
		for y1 in range(M):
			visited[str(x1)+"x"+str(y1)]=0
	count=[0]
	paths2(x,y,visited,1,count,N,M)
	return count[0]
def paths2(x,y,visited,numVisited,count,N,M):
	if x<0 or x>=N or y<0 or y>=M or (visited[str(x)+"x"+str(y)]==1):
		return
	visited[str(x)+"x"+str(y)]=1
	try:
		if (x == 0 and y == (M - 1)):
			if (numVisited == N * M):
				count[0]+=1
			return
		numVisited+=1
		paths2(x, y + 1, visited, numVisited, count,N,M)
		paths2(x + 1, y, visited, numVisited, count,N,M)
		paths2(x - 1, y, visited, numVisited, count,N,M)
		paths2(x, y - 1, visited, numVisited, count,N,M)
	finally: 
		visited[str(x)+"x"+str(y)]=0
main()