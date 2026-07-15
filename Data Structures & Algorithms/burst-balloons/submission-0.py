class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        tnums = [1] + nums + [1]
        memo = {}
        def dfs(l, r):
            if l > r:
                return 0
            state = (l, r)
            if state in memo:
                return memo[state]
            res = 0
            for i in range(l, r + 1):
                gain = tnums[l - 1] * tnums[i] * tnums[r + 1]
                gain += dfs(l, i - 1) + dfs(i + 1, r)
                res = max(res, gain)
            memo[state] = res
            return res
        return dfs(0, len(nums) - 1)