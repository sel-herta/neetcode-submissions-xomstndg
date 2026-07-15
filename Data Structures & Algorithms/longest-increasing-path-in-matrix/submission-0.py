class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            state = (i, j)
            if state in memo:
                return memo[state]
            tres = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[i][j] < matrix[ni][nj]:
                        res = 1 + dfs(ni, nj)
                        tres = max(tres, res)
            memo[state] = tres
            return tres
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans
        
        