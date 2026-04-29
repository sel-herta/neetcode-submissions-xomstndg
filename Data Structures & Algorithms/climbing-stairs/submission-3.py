class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            res = dfs(i+1)+dfs(i+2)
            memo[i] = res
            return res
        return dfs(0)