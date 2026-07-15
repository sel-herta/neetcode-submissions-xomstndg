class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            state = (i, curr_sum)
            if state in memo:
                return memo[state]
            add = dfs(i + 1, curr_sum + nums[i])
            sub = dfs(i + 1, curr_sum - nums[i])
            res = add + sub
            memo[state] = res
            return res
        return dfs(0, 0)