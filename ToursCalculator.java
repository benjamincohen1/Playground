public class ToursCalculator {
    public int M;
    public int N;
    public ToursCalculator(int M, int N) {
        this.M = M;
        this.N = N;
    }
    private void paths(int x, int y, boolean[][] visited, int numVisited, int[] count) {
        if ( y < 0 || y >= N || x < 0 || x >= M || visited[x][y]) //out of bounds or already done
            return;
        visited[x][y] = true;
        try {
            if (x==0 && y==N-1) {
                if (numVisited == M * N)  //last state we need to visit
                    count[0]++;
                return;
            }
            numVisited++; //add one to the states visited
            /*Try all of the alternatives*/
            paths(x, y+1, visited, numVisited, count);
            paths(x+1, y, visited, numVisited, count);
            paths(x,y-1, visited, numVisited, count);
            paths(x-1, y, visited, numVisited, count);
        } 
        finally {
            visited[x][y] = false; //Set the state back to false so we can look at it again later
        }
    }

    public int paths(int x, int y) {
        boolean[][] visited = new boolean[M][N];
        int[] count = {0};
        paths(x, y, visited, 1,  count);
        return count[0];
    }

    public static void main(String args[]){
        ToursCalculator t = new ToursCalculator(Integer.parseInt(args[0]),Integer.parseInt(args[1]));
        int numPaths = t.paths(0, 0);
        System.out.print("Found "+numPaths+" paths.");
    }
}