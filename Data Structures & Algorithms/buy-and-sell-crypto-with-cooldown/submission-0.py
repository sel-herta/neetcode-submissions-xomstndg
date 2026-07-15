class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            state = (i, buy)
            if state in memo:
                return memo[state]
            skip = dfs(i + 1, buy)
            use = 0
            sell = 0
            if buy:
                use = dfs(i + 1, False) - prices[i]
            else:
                sell = dfs(i + 2, True) + prices[i]
            res = max(skip, use, sell)
            memo[state] = res
            return res
        return dfs(0, True)
