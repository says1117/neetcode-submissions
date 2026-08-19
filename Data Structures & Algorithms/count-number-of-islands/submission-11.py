class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direct = [(-1,0), (1,0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        numIsl = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                curR, curC = q.popleft()

                for dr, dc in direct:
                    newR, newC = curR + dr, curC + dc
                    if (newR,newC) not in visit and newR >=0 and newC >= 0 and newR < rows and newC < cols and grid[newR][newC] == '1':
                        q.append((newR, newC))
                        visit.add((newR,newC))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    numIsl+=1

        return numIsl

