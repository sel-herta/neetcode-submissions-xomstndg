class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            grid[i][j] = "0"
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if not 0 <= nr < rows or not 0 <= nc < cols:
                    continue
                if grid[nr][nc] == '0':
                    continue
                dfs(nr, nc)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res