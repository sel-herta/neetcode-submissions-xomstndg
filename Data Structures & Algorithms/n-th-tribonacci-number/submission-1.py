class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i in cache:
                return cache[i]
            res = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            cache[i] = res
            return res
        return dfs(n)