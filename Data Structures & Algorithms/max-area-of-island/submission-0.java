class Pair{
    public int x;
    public int y;

    public Pair(int row, int col){
        x = row;
        y = col;
    }
}

class Solution {
    public int r;
    public int c;
    public int numIsl = 0;

    public int maxAreaOfIsland(int[][] grid) {
        r = grid.length;
        c = grid[0].length;

        boolean[][] visited = new boolean[r][c];
        int area = 0;

        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(!visited[i][j] && inbounds(i,j) && grid[i][j] == 1){
                    numIsl++;
                    int max = bfs(grid, visited, i, j);
                    area = Math.max(max, area);
                }
            }
        }

        return area;
        
    }

    public int bfs(int[][] grid, boolean[][] visited, int rows, int cols){
        LinkedList<Pair> q = new LinkedList<Pair>();

        //up down left right
        int[] DX = {-1,1,0,0};
        int[] DY = {0,0,-1,1};

        q.offer(new Pair(rows, cols));
        visited[rows][cols] = true;
        int num = 1;

        while(q.size() > 0){
            Pair p = q.poll();

            for(int i=0; i<4; i++){
                int newR = p.x+DX[i];
                int newC = p.y+DY[i];

                if(inbounds(newR,newC) && !visited[newR][newC] && grid[newR][newC] == 1){
                    q.offer(new Pair(newR, newC));
                    visited[newR][newC] = true;
                    num++;
                }
            }

        }
        return num;
    }

    public boolean inbounds(int newR, int newC){
        if(newR >= 0 && newR < r && newC >=0 && newC < c){
            return true;
        }
        return false;
    }
}
