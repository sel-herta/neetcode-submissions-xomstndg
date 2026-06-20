class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque()
        ans = 0
        fruits = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fruits += 1
        while q:
            ci, cj, ctime = q.popleft()
            ans = max(ans, ctime)
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == 1:
                        fruits -= 1
                        grid[ni][nj] = 2
                        q.append((ni, nj, ctime + 1))
        if fruits == 0:
            return ans
        else:
            return -1