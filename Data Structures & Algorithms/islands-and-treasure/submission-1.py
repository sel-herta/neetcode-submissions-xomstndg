class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, curDist = q.popleft()
            grid[i][j] = min(grid[i][j], curDist)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if (ni, nj) not in visited:
                        if grid[ni][nj] != -1:
                            visited.add((ni, nj))
                            q.append((ni, nj, curDist + 1))