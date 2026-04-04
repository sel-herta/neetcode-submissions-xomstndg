class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {} # position : possible

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in cache:
                return cache.get((i, j))
            res = dfs(i + 1, j) + dfs(i, j + 1)
            cache[(i, j)] = res
            return res
        
        return dfs(0, 0)