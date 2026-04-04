class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        numStairs = len(cost) + 2
        dp = [0] * numStairs

        for i in range(len(dp) - 3, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])
        return min(dp[0], dp[1])