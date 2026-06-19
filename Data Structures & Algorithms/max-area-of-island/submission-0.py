class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def dfs(i, j):
            res = 1
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited:
                        if grid[nr][nc] == 1:
                            visited.add((nr, nc))
                            res += dfs(nr, nc)
            return res
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    ans = max(ans, dfs(i, j))
        return ans