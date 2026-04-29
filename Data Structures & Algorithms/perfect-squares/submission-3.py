sys.setrecursionlimit(1000000)

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i < 0:
                return float('inf')
            if i in memo:
                return memo[i]
            res = float('inf')
            for j in range(1, i + 1):
                sq = j * j
                if sq > i:
                    break
                tres = 1 + dfs(i - sq)
                res = min(res, tres)
            memo[i] = res
            return res
        return dfs(n)