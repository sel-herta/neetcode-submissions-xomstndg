class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {} # stair : ways

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache.get(i)
            res = dfs(i + 1) + dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)