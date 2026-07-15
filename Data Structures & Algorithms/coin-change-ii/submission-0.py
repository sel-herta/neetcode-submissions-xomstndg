class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if total >= amount:
                return 1 if total == amount else 0
            if i == len(coins):
                return 0
            state = (i, total)
            if state in memo:
                return memo[state]
            skip = dfs(i + 1, total)
            use = dfs(i, total + coins[i])
            res = skip + use
            memo[state] = res
            return res
        return dfs(0, 0)