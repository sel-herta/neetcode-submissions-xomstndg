class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(curAmount):
            if curAmount == 0:
                return 0
            if curAmount in memo:
                return memo[curAmount]
            res = float('inf')
            for coin in coins:
                if curAmount - coin >= 0:
                    res = min(res, 1 + dfs(curAmount - coin))
            memo[curAmount] = res
            return res
        ans = dfs(amount)
        return -1 if ans == float('inf') else ans
            