public class ToursCalculator {
    public int width;
    public int height;
    public ToursCalculator(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int countPaths(int x, int y) {
        boolean[][] visited = new boolean[width][height];
        int[] count = {0};
        countPaths(x, y, visited, 1,  count);
        return count[0];
    }

    private void countPaths(int x, int y, boolean[][] visited, int depth, int[] count) {
        if (x < 0 || x >= width || y < 0 || y >= height || visited[x][y])
            return;
        visited[x][y] = true;
        try {
            if (x == 0 && y == height - 1) {
                if (depth == width * height)
                    count[0]++;
                return;
            }
            countPaths(x, y + 1, visited, depth+1, count);
            countPaths(x + 1, y, visited, depth+1, count);
            countPaths(x - 1, y, visited, depth+1, count);
            countPaths(x, y - 1, visited, depth+1, count);
        } 
        finally {
            visited[x][y] = false;
        }
    }

    public static void main(String args[]) {
        long start = System.nanoTime();
        ToursCalculator cp = new ToursCalculator(args[0],args[1]);
        int count = cp.countPaths(0, 0);
        long time = System.nanoTime() - start;
        System.out.printf("%,d paths found in %.3f seconds.%n", count, time / 1e9);
    }
}