class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(i, j):
            nonlocal ans
            q = deque()
            seen.add((i, j))
            q.append((i, j))
            while q:
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or nj < 0 or ni == rows or nj == cols or grid[ni][nj] == 0:
                        ans += 1
                    elif (ni, nj) not in seen:
                        seen.add((ni, nj))
                        q.append((ni, nj))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in seen:
                    bfs(i, j)
        return ans

