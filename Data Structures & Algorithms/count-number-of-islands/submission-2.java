class Pair{
    public int x;
    public int y;

    public Pair(int row, int col){
        x=row;
        y=col;
    }
}

class Solution {

    //up down left right
    public int[] DX = {-1, 1, 0, 0};
    public int[] DY = {0, 0, -1, 1};
    public int numIsl;

    public int numIslands(char[][] grid) {
        int rLen = grid.length;
        int cLen = grid[0].length;
        LinkedList<Pair> q = new LinkedList<>();
        boolean[][] visited = new boolean[rLen][cLen];
        numIsl = 0;

        for(int i=0; i<rLen; i++){
            for(int j=0; j<cLen; j++){
                if(grid[i][j] == '1' && !visited[i][j]){
                    q.offer(new Pair(i,j));
                    visited[i][j]=true;

                    while(q.size() > 0){
                        Pair p = q.poll();

                        for(int h=0; h<4; h++){
                            int newR = p.x+DX[h];
                            int newC = p.y+DY[h];

                            if(inbounds(rLen, cLen, newR, newC) && grid[newR][newC] == '1' && !visited[newR][newC]){
                                q.offer(new Pair(newR, newC));
                                visited[newR][newC] = true;
                            }
                        }
                    }
                    numIsl++;
                }
            }
        }
        return numIsl;
    }

    public boolean inbounds(int rLen, int cLen, int x, int y){
        if(x >= 0 && x < rLen && y >= 0 && y < cLen){
            return true;
        }
        return false;
    }
}
